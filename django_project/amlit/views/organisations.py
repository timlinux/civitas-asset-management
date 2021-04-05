__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/03/21'

from django.core.exceptions import PermissionDenied
from django.forms.models import model_to_dict
from django.views.generic import ListView
from django.views.generic.edit import UpdateView
from amlit.models.organisation import Organisation, UserOrganisation
from amlit.forms.organisation import OrganisationFormForOwner, UserOrganisationForm

from amlit.models.subscription import Plan


class OrganisationListView(ListView):
    template_name = 'organisations/list.html'
    model = Organisation

    def get_queryset(self):
        return Organisation.by_user.all_role(self.request.user)


class OrganisationView(UpdateView):
    model = Organisation
    template_name = 'organisations/edit.html'
    form_class = OrganisationFormForOwner
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super(OrganisationView, self).get_context_data(**kwargs)
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

        # context plan
        context['plans'] = Plan.objects.all()
        return context
