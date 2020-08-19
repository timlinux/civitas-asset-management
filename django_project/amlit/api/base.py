__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '19/08/20'

from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import get_object_or_404


class SingleObjectAPI(APIView):
    """
    get:
    Return geojson of feature
    """
    Model = None
    Serializer = None

    def get(self, request, id):
        """ Return data of feature """
        return Response(
            self.Serializer(
                get_object_or_404(self.Model, pk=id)
            ).data
        )


class MultiObjectAPI(APIView):
    """
    get:
    Return geojson of feature
    """
    Model = None
    Serializer = None

    def get(self, request):
        """ Return data of features """
        return Response(
            self.Serializer(
                self.Model.objects.all(), many=True
            ).data
        )
