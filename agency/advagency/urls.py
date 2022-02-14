from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employment_department', views.employment_department, name='employment_department'),
    path('employment_department/<str:position_code>', views.employment_department, name='employment_department'),
    path('places/', views.places_types, name='places_types'),
    path('places/<str:type_code>', views.places_types, name='places_types'),
]
