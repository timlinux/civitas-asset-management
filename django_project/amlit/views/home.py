__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '13/09/19'

from django.views.generic import TemplateView
from amlit_helpdesk.views.public import create_ticket


class HomeView(TemplateView):
    template_name = 'home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        view = create_ticket(self.request, self.args, **kwargs)
        context['create_ticket_form'] = view.context_data['form']
        return context
