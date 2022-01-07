from django.shortcuts import render
from places.models import Place


def index(request):
    place_data_2 = {
        "type": "FeatureCollection",
        "features": []}
    all_places = Place.objects.all()
    for place in all_places:
        place_data_2['features'].append(
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
        'all_places': place_data_2,
    }
    return render(request, 'index.html', context)
