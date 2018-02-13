from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
import googlemaps
from django.http import HttpResponse, JsonResponse
import json
from ft.models import *
from ft.api.serializers import *



def locationSave(request,lat,lng,city):

	posi = Position(lng = lng,lat = lat)
	posi.save()
	ct = City(city_name = city,pos =posi)
	ct.save()
	location = {}
	location["city"] = ct.city_name
	location["posi"] = posi.id
	print(location)
	return JsonResponse(location)

'''
class AllCityViewSet(viewsets.ModelViewSet):

	serializer_class = CitySerializer

	def get_queryset(self):
		ct = City.objects.filter(city_name__contains = self.kwargs["name"])
		if len(ct) != 0 :
			city_dict["city_name"] = {}
			for c in ct :
				city_dict["city_name"].append(c.city_name)
		return JsonResponse(city_dict)
'''
def allcity(request,name):
	ct = City.objects.filter(city_name__contains = name)
	if len(ct) != 0 :
		city_dict = {}
		city_dict["city_name"] = []
		for c in ct :
			city_dict["city_name"].append(c.city_name)
	return JsonResponse(city_dict)