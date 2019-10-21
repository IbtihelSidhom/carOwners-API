from rest_framework.generics import ListAPIView
from owners.models import Owner
from .serializers import OwnerSerializer

class OwnerListView(ListAPIView):
    queryset = Owner.objects.all()
    serializer_class = OwnerSerializer