from rest_framework import viewsets
from rest_framework.views import APIView
from django.views.generic import CreateView
from rest_framework.response import Response
import googlemaps
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from ft.models import *
from ft.api.serializers import *


class AllCityViewSet(viewsets.ModelViewSet):

	serializer_class = CitySerializer

	def get_queryset(self):
		return City.objects.filter(city_name__contains = self.kwargs["name"])
		
class LocationSaveViewSet(APIView):
	
	def post(self, request):
		j = json.loads(request.body.decode("utf-8"))
		posi = Position(lng = j["lng"],lat = j["lat"])
		posi.save()
		ct = City(city_name = j["city"],pos =posi)
		ct.save()
		location = {}
		location["city"] = ct.city_name
		location["posi"] = posi.id
		return JsonResponse(location)

