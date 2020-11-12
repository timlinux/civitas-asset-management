__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '09/09/20'

from rest_framework.response import Response
from rest_framework.views import APIView
from amlit.utilities.feature_summary import SummaryReport


class SummaryAPI(APIView):
    """
    get:
    Return json of summary API
    """

    def get(self, request):
        """ Return data of features """
        return Response(
            SummaryReport().summary())
