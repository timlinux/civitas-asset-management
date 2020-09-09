__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from datetime import datetime
from django.http import HttpResponseBadRequest
from rest_framework.response import Response
from rest_framework.views import APIView
from amlit.utils.financial_report import ProjectedReport


class ProjectedReportAPI(APIView):
    """
    get:
    Return json of projected API
    """

    def get(self, request, year):
        """ Return data of features """
        try:
            date = datetime.today()
            date = date.replace(year=int(year))
            th_year = int(year) - datetime.today().year
            if th_year < 1:
                return HttpResponseBadRequest('Year need to be in future')
        except ValueError:
            return HttpResponseBadRequest('Year is not integer')

        return Response(ProjectedReport(date).get())
