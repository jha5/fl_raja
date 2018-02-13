from django.shortcuts import render
import googlemaps
from datetime import datetime
# Create your views here.
gmaps = googlemaps.Client(key='AIzaSyAcxXmnYcC0EXVN84lYpgs0PvTXoiV6fns')

def LocationSave(request, pk):