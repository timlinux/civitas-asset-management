__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/20'

from rest_framework.response import Response
from rest_framework.views import APIView
from amlit.models.view.feature_calculations import FeatureCalculation
from amlit.serializer.features import FeatureGeoSerializer


class FeaturesGeojsonAPI(APIView):
    """
    get:
    Return geojson of features
    """

    def get(self, request):
        """ Return data of features """
        systems = request.GET.get('systems', '').split(',')
        query = FeatureCalculation.objects.filter(feature__system__id__in=systems)
        return Response(
            FeatureGeoSerializer(query, many=True).data
        )
