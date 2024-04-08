import random  # Import the random module
from django.shortcuts import render
from django.views import View
from .models import Locations, driver  # Import the Driver model

class MapView(View):
    template_name = "myMap/map.html"

    def get(self, request):
        key = 'AIzaSyC3Zcg-Rod-bnXvODcqRry4g7Soz5AdjDU'
        eligible_locations = Locations.objects.filter(place_id__isnull=False)
        locations = []

        for location in eligible_locations:
            data = {
                'lat': float(location.lat),
                'lng': float(location.lng),
                'name': location.name
            }
            locations.append(data)

        # Select one random driver
        drivers = list(driver.objects.all())
        selected_driver = None
        if drivers:
            selected_driver = random.choice(drivers)

        context = {
            "key": key,
            "locations": locations,
            "selected_driver": selected_driver,
        }
        return render(request, self.template_name, context)
