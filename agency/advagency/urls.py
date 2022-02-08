from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('employment_department', views.employment_department, name='emp_dep'),
    path('employment_department/<str:position_code>', views.employment_department, name='emp_dep'),
    path('places/', views.places_handler),
    path('places/<str:type_code>', views.places_types),
    # path('places_by_type/', views.illnesses_by_drugs)
]
