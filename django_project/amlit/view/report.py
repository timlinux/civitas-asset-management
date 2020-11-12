__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '04/09/20'

from django.views.generic.base import TemplateView
from amlit.utilities.feature_summary import FinancialReport


class ReportPageView(TemplateView):
    template_name = "report.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['reports'] = FinancialReport().summary_all()
        return context
