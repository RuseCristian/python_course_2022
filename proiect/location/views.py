from django.shortcuts import render, redirect
from django.urls import reverse
from django.views.generic import ListView, CreateView, UpdateView

from location.models import Location


# Create your views here.
class LocationView(ListView):
    model = Location
    template_name = 'location/location_index.html'



class CreateLocationView(CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')


class UpdateLocationView(UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')


def delete_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect('location:lista_locatii')


def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect('location:lista_locatii')