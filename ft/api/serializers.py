from ft.models import *
from rest_framework import serializers

class PositionSerializer(serializers.ModelSerializer):
	
	class Meta:
		model = Position
		fields = ("id","lng","lat")

class CitySerializer(serializers.ModelSerializer):

	id = serializers.CharField(max_length = 20, required = False)
	position = PositionSerializer(required = False)

	class Meta:
		model = City
		fields = ("id","city_name","position")