from django.shortcuts import render
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from django.core import serializers
from django.http import JsonResponse


def index(request):
    place_data = {
        "type": "FeatureCollection",
        "features": []}
    all_places = Place.objects.all()
    for place in all_places:
        place_data['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": "./static/places/moscow_legends.json"
                }
            },
        )

    context = {
        'all_places': place_data,
    }
    return render(request, 'index.html', context)


def places(request, place_id):
    need_place = Place.objects.filter(pk=place_id)
    need_place_images = [str(image) for image in need_place.first().images.all()]
    need_place_json = list(need_place.values())
    need_place_json[0]['imgs'] = need_place_images
    return JsonResponse(
        need_place_json,
        safe=False,
        json_dumps_params={'indent': 2, 'ensure_ascii': False})

