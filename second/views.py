from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from second.models import *
from second.serializers import *


# Create your views here.
class CarAPIFull(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarFullSerializer

class BoatAPIFull(ModelViewSet):
    queryset = Boat.objects.all()
    serializer_class = BoatFullSerializer
