__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '11/11/20'

from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from amlit.models.community import Community
from amlit.serializer.community import (
    CommunitySerializer, CommunityDetailSerializer
)


class CommunityAPI(APIView):
    """ Return community list """

    def get(self, request):
        """ Return data of features """
        return Response(
            CommunitySerializer(
                Community.objects.filter(geometry__isnull=False).order_by('name'), many=True
            ).data
        )


class CommunityDetailAPI(APIView):
    """ Return community list """

    def get(self, request, id):
        """ Return data of features """
        return Response(
            CommunityDetailSerializer(
                get_object_or_404(Community, pk=id)
            ).data
        )
