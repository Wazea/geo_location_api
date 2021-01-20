import os
import gmplot
import requests
from requests import RequestException


class CoordinatesPlotter:
    @staticmethod
    def plot_coordinates_on_map():

        # apikey = ''
        # gmap = gmplot.GoogleMapPlotter(37.766956, -122.448481, 14, apikey=apikey)
        # gmap.marker(37.770776, -122.461689, color='cornflowerblue')
        #
        # attractions_lats, attractions_lngs = zip(*[
        #     (37.769901, -122.498331),
        #     (37.768645, -122.475328),
        #     (37.771478, -122.468677),
        #     (37.769867, -122.466102),
        #     (37.767187, -122.467496),
        #     (37.770104, -122.470436)
        # ])
        #
        # gmap.scatter(attractions_lats, attractions_lngs, color='#3B0B39', size=40, marker=False)
        #
        # golden_gate_park = zip(*[
        #     (37.771269, -122.511015),
        #     (37.773495, -122.464830),
        #     (37.774797, -122.454538),
        #     (37.771988, -122.454018),
        #     (37.773646, -122.440979),
        #     (37.772742, -122.440797),
        #     (37.771096, -122.453889),
        #     (37.768669, -122.453518),
        #     (37.766227, -122.460213),
        #     (37.764028, -122.510347)
        # ])
        #
        # gmap.polygon(*golden_gate_park, color='cornflowerblue', edge_width=10)
        #
        # gmap.draw('map.html')
        # os.system('map.html')

        try:
            response = requests.get("https://api.thingspeak.com/channels/1273540/fields/1.json?api_key"
                                    "=6VD0YT9MCMAD5ER3&results=2")
            response.raise_for_status()
            print(response)

            response_json = response.json()
            print('Latitude: ' + response_json["channel"]["latitude"])
            print('Longitude: ' + response_json["channel"]["longitude"])
        except RequestException:
            print('Request not satisfied!')
