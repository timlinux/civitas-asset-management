__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '08/03/21'

from django.http import JsonResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from amlit_helpdesk.models.feature_ticket import FeatureTicket
from civitas.models.feature.feature_geometry import FeatureGeometry
from civitas.serializer.features import FeatureGeometryGeoSerializer
from helpdesk.serializers import DatatablesTicketSerializer


class FeatureTicketListView(ListAPIView):
    """
    Return of tickets list of feature
    """

    serializer_class = DatatablesTicketSerializer
    model = serializer_class.Meta.model
    paginate_by = 100

    def get_queryset(self):
        feature_id = self.kwargs['id']
        queryset = FeatureTicket.objects.filter(feature_id=feature_id).values_list('ticket', flat=True)
        queryset = self.model.objects.filter(id__in=queryset)
        return queryset.order_by('-created')


class FeatureTicketFeatureDetailAPI(APIView):
    """
    Return Detail Asset of ticket
    """

    def get(self, request, id, *args):
        feature_ticket = get_object_or_404(FeatureTicket, ticket_id=id)
        feature = get_object_or_404(FeatureGeometry, id=feature_ticket.feature_id)
        return JsonResponse(FeatureGeometryGeoSerializer(feature).data)