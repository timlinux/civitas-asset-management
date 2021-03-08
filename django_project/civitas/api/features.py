__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '18/11/20'

from rest_framework.response import Response
from rest_framework.views import APIView
from civitas.models.feature.feature_geometry import FeatureGeometry
from civitas.serializer.features import FeatureGeometryGeoSerializer


class FeaturesGeojsonAPI(APIView):
    """
    get:
    Return geojson of features
    """

    def get(self, request):
        """ Return data of features """
        systems = request.GET.get('systems', '').split(',')
        query = FeatureGeometry.objects.filter(feature__system__id__in=systems)
        return Response(
            FeatureGeometryGeoSerializer(query, many=True).data
        )
