from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView
from django.urls import reverse
from location.models import Location
from django.views.generic.edit import UpdateView


class LocationView(LoginRequiredMixin, ListView):
    model = Location
    template_name = 'location/location_index.html'


class CreateLocationView(LoginRequiredMixin, CreateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')


class UpdateLocationView(LoginRequiredMixin, UpdateView):
    model = Location
    fields = ['city', 'country']
    template_name = 'location/location_form.html'

    def get_success_url(self):
        return reverse('location:lista_locatii')


@login_required
def delete_location(request, pk):
    Location.objects.filter(id=pk).update(active=0)
    return redirect('location:lista_locatii')


@login_required
def activate_location(request, pk):
    Location.objects.filter(id=pk).update(active=1)
    return redirect('location:lista_locatii')
