from django.urls import path

from location import views

app_name = 'location'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),

]
