import json
from django.core import serializers
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from .models import Employee, Position, Place, AdvertisementType
from .utils import dict_from_queryset


def index(request):
    return HttpResponse(render(request, 'advagency/index.html'))


def employment_department(request, position_code=None):
    print(position_code)
    all_positions = Position.objects.all()
    positions = dict_from_queryset(
        Position.objects.all() if position_code is None else Position.objects.filter(code=position_code)
    )
    for p in positions:
        pos_employees = dict_from_queryset(Employee.objects.filter(position_code=p['code']))
        p['employees'] = pos_employees

    print(positions)
    context = {
        'positions': positions,
        'all_positions': all_positions,
        'position_code': position_code,
    }

    return HttpResponse(render(request, 'advagency/emp_dep.html', context))


def places_handler(request):
    places = dict_from_queryset(Place.objects.all())
    for p in places:
        print(p)
        p['type'] = dict_from_queryset(AdvertisementType.objects.filter(code=p['type_code_id']))[0]
    context = {
        'places': places,
    }
    return HttpResponse(render(request, 'advagency/places.html', context))


def places_types(request, type_code=None):
    types = dict_from_queryset(
        AdvertisementType.objects.all() if type_code is None else AdvertisementType.objects.filter(code=type_code)
    )
    for t in types:
        type_places = dict_from_queryset(Place.objects.filter(type_code=t['code']))
        t['places'] = type_places

    print(types)  # dict of needed info
    return HttpResponse(types)


def illnesses(request):
    ill = dict_from_queryset(Illness.objects.all())
    drugs = dict_from_queryset(Drug.objects.all())
    for drug in drugs:
        for il in ill:
            drug_code = drug['code']
            for drug_field in ['drug1_code_id', 'drug2_code_id', 'drug3_code_id']:
                if il[drug_field] == drug_code:
                    il[drug_field] = drug
    return HttpResponse(ill)

