import json
import djstripe
import stripe

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.forms.models import model_to_dict
from django.http import JsonResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView

from amlit.models.organisation import Organisation, UserOrganisation
from amlit.forms.organisation import (
    OrganisationFormForOwner, UserOrganisationForm)
from amlit.utils import AmlitStripe


class OrganisationListView(LoginRequiredMixin, ListView):
    """ Showing list of organisation of an user
    """
    template_name = 'organisations/list.html'
    model = Organisation

    def get_queryset(self):
        return Organisation.by_user.all_role(self.request.user)


class OrganisationEditView(LoginRequiredMixin, UpdateView):
    """ Showing Organisation view to be updated
    """
    model = Organisation
    template_name = 'organisations/edit.html'
    form_class = OrganisationFormForOwner
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(OrganisationEditView, self).get_context_data(**kwargs)
        if not self.object.is_admin(self.request.user):
            raise PermissionDenied('You do not have permission.')

        users = {
            'form': UserOrganisationForm(),
            'data': []
        }
        for user_org in UserOrganisation.objects.filter(organisation=self.object):
            users['data'].append(
                UserOrganisationForm(initial=model_to_dict(user_org), instance=user_org)
            )
        context['users'] = users
        return context


class SubscriptionView(LoginRequiredMixin, DetailView):
    """ Subscription view for an organisation
    """
    template_name = "organisations/subscription.html"
    model = Organisation

    def get_context_data(self, **kwargs):
        context = super(SubscriptionView, self).get_context_data(**kwargs)
        if not self.object.is_owner(self.request.user):
            raise PermissionDenied('You do not have permission.')

        context['products'] = AmlitStripe().products()
        context['STRIPE_PUBLIC_KEY'] = AmlitStripe().public_key
        return context

    def post(self, request, *args, **kwargs):
        organisation = self.get_object()
        data = json.loads(request.body)
        stripe.api_key = AmlitStripe().secret_key

        payment_method = data['payment_method']
        payment_method_obj = stripe.PaymentMethod.retrieve(payment_method)
        djstripe.models.PaymentMethod.sync_from_stripe_data(payment_method_obj)

        try:
            # This creates a new Customer and attaches the PaymentMethod in one API call.
            customer = stripe.Customer.create(
                payment_method=payment_method,
                email=request.user.email,
                invoice_settings={
                    'default_payment_method': payment_method
                }
            )
            djstripe.models.Customer.sync_from_stripe_data(customer)

            # Subscribe
            subscription = stripe.Subscription.create(
                customer=customer.id,
                items=[
                    {"price": data["price_id"]},
                ],
                expand=["latest_invoice.payment_intent"]
            )

            djstripe_subscription = djstripe.models.Subscription.sync_from_stripe_data(subscription)

            organisation.subscription = djstripe_subscription
            organisation.save()
            return JsonResponse({'Result': 'OK'})

        except Exception as e:
            return JsonResponse({'error': (e.args[0])}, status=403)


class SubscriptionCompleteView(LoginRequiredMixin, DetailView):
    """ Page when subscription is completed
    """
    template_name = "organisations/complete.html"
    model = Organisation
