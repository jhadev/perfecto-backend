from wines.models import Wine
from wines.serializers import WineSerializer
from rest_framework import generics


class WineListCreate(generics.ListCreateAPIView):
    queryset = Wine.objects.all()
    serializer_class = WineSerializer
