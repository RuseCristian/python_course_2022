from django.urls import path

from location import views

app_name = 'location'

urlpatterns = [
    path('', views.LocationView.as_view(), name='lista_locatii'),
    path('adaugare/', views.CreateLocationView.as_view(), name='adaugare'),
    path('<int:pk>/update/', views.UpdateLocationView.as_view(), name='modificare'),

    path('<int:pk>/delete/', views.delete_location, name='stergere'),
    path('<int:pk>/activate/', views.activate_location, name='activare'),
]