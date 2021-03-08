__author__ = 'Irwan Fathurrahman <meomancer@gmail.com>'
__date__ = '08/03/21'

from rest_framework.generics import ListAPIView

from amlit_helpdesk.models.feature_ticket import FeatureTicket
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
