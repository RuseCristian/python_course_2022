from django.shortcuts import render
from django.views.generic import ListView

from proiect.location.models import Location


# Create your views here.

class LocationVeiw(ListView):
    model = Location
    template_name = 'location/location_index.html'
