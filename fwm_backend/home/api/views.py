from rest_framework import viewsets
from home.api.serializers import ContributionSerializer
from home.models import Contribution


class ContributionViewSet(viewsets.ModelViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer

