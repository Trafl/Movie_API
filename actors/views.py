from rest_framework import generics
from actors.models import Actors
from actors.serializers import ActorsSerializer


class ActorsCreateListAPIView(generics.ListCreateAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer


class ActorsRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Actors.objects.all()
    serializer_class = ActorsSerializer
