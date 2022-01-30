from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.shortcuts import get_object_or_404

from places.models import Place


def index(request):
    geojson_for_template = {
        "type": "FeatureCollection",
        "features": []}
    all_places = Place.objects.all()
    for place in all_places:
        geojson_for_template['features'].append(
            {
                "type": "Feature",
                "geometry": {
                    "type": "Point",
                    "coordinates": [place.lng, place.lat]
                },
                "properties": {
                    "title": place.title,
                    "placeId": place.pk,
                    "detailsUrl": reverse('place', args=[place.pk])
                }
            },
        )

    context = {
        'all_places': geojson_for_template,
    }
    return render(request, 'index.html', context)


def places(request, place_id):
    needed_place = get_object_or_404(Place, pk=place_id)
    needed_place_images = [str(image) for image in needed_place.images.all()]
    needed_place_raw = list(needed_place.values())
    needed_place_raw[0]['imgs'] = needed_place_images
    return JsonResponse(
        needed_place_raw[0],
        safe=False,
        json_dumps_params={'indent': 2, 'ensure_ascii': False})

