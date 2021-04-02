__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '13/09/19'

from django.views.generic import TemplateView
from helpdesk.forms import PublicTicketForm


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['create_ticket_form'] = PublicTicketForm()
        return context
