from django.shortcuts import render
from django.http import HttpResponse

from .models import Employee, Position, Place, AdvertisementType
from .utils import get_dict


def index(request):
    return HttpResponse(render(request, 'advagency/index.html'))


def employment_department(request, position_code=None):
    all_positions = Position.objects.all()
    positions = get_dict(
        Position.objects.all() if position_code is None else Position.objects.filter(code=position_code)
    )
    for p in positions:
        pos_employees = get_dict(Employee.objects.filter(position_code=p['code']))
        p['employees'] = pos_employees
    context = {
        'positions': positions,
        'all_positions': all_positions,
        'position_code': position_code,
    }
    return HttpResponse(render(request, 'advagency/employment.html', context))


def places_types(request, type_code=None):
    all_types = AdvertisementType.objects.all()
    types = get_dict(
        AdvertisementType.objects.all() if type_code is None else AdvertisementType.objects.filter(code=type_code)
    )
    for t in types:
        type_places = get_dict(Place.objects.filter(type_code=t['code']))
        t['places'] = type_places
    context = {
        'types': types,
        'all_types': all_types,
        'type_code': type_code,
    }
    return HttpResponse(render(request, 'advagency/places.html', context))
