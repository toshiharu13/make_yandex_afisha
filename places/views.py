from django.shortcuts import render
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


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
    need_place = get_object_or_404(Place, pk=place_id)
    return HttpResponse(need_place.title)

