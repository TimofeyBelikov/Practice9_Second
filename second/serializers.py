
from rest_framework import serializers

from second.models import *


class CarFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"

class BoatFullSerializer(serializers.ModelSerializer):
    class Meta:
        model = Boat
        fields = "__all__"