__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '08/03/21'

from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.generics import ListAPIView
from rest_framework.views import APIView

from amlit_helpdesk.models.feature_ticket import FeatureTicket
from civitas.models.feature.feature_geometry import FeatureBase
from civitas.serializer.features import FeatureGeometryGeoSerializer
from helpdesk.serializers import DatatablesTicketSerializer
from helpdesk.models import Ticket


class AmlitDatatablesTicketSerializer(DatatablesTicketSerializer):
    class Meta:
        model = Ticket
        # fields = '__all__'
        fields = ('ticket', 'id', 'priority', 'title', 'queue', 'status',
                  'created', 'due_date', 'assigned_to', 'submitter', 'row_class',
                  'time_spent', 'kbitem', 'description')


class TicketListView(ListAPIView):
    """
    Return of tickets list of community
    """

    serializer_class = AmlitDatatablesTicketSerializer
    model = serializer_class.Meta.model
    paginate_by = 100

    def get_queryset(self):
        queryset = FeatureTicket.objects.values_list('ticket', flat=True)
        queryset = self.model.objects.filter(id__in=queryset)
        return queryset.order_by('-created')


class FeatureTicketListView(ListAPIView):
    """
    Return of tickets list of feature
    """

    serializer_class = DatatablesTicketSerializer
    model = serializer_class.Meta.model
    paginate_by = 100

    def get_queryset(self):
        feature_id = self.kwargs['id']
        queryset = FeatureTicket.objects.filter(
            feature_id=feature_id).values_list('ticket', flat=True)
        queryset = self.model.objects.filter(id__in=queryset)
        return queryset.order_by('-created')


class FeatureTicketFeatureDetailAPI(APIView):
    """
    Return Detail Asset of ticket
    """

    def get(self, request, id, *args):
        feature_ticket = get_object_or_404(FeatureTicket, ticket_id=id)
        feature = get_object_or_404(FeatureBase, id=feature_ticket.feature_id)
        return JsonResponse(FeatureGeometryGeoSerializer(feature).data)
