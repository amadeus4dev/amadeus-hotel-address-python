## Get an address from latitude/longitude

In this tutorial we will show you how you can translate a latitude/longitude location into a readable address using Python. We will use the method of `Reverse Geocoding` and then we will use the `Google Places API`. 

### Method 1: Reverse Geocoding

Reverse geocoding is the process of converting geographic coordinates (i.e. latitude and longitude) to a readable address. The accuracy in reverse geocoding might vary depending on the quality and availability of the data sources.

For this tutorial we explore two providers and make their requests using the [Geocoder](https://geocoder.readthedocs.io/) library. The library allows you to use several providers such as Google Maps, OpenStreetMap and Bing Maps.

Before moving forward make sure you install the library in your environment with `pip install geocoder`. 

#### Google Geolocation API

The [Google Geolocation API](https://developers.google.com/maps/documentation/geolocation/overview) uses data from various sources, such cell towers and Wi-Fi access points to determine the address of a geolocation. 

In order to use Google you will need to create an account and then export your key in your environment variables 

```
export GOOGLE_API_KEY=YOUR_KEY
```

And then write the code below to get the address of the location with coordinates `48.8682, 2.33395`:

```python
import geocoder

lat_lng = [48.8682, 2.33395]
response = geocoder.google(lat_lng, method='reverse')

print(response.json['address'])
```

#### OpenStreetMap 

[OpenStreetMap](https://www.openstreetmap.org/#map=6/40.028/-2.417) is an open-source project that relies on contributions from volunteers to create and maintain a free map of the world. Its data is primarily collected by volunteers through GPS devices and aerial imagery.

Let's see now see a code example how to get the address of the `48.8682, 2.33395` location:

```python
import geocoder

lat_lng = [48.8682, 2.33395]
response = geocoder.osm(lat_lng, method='reverse')

print(response.json['address'])
```

### Method 2: Google Places API

The [Google Places API](https://developers.google.com/maps/documentation/places/web-service/overview) returns information about specific places, such as businesses and landmarks, that have been verified by Google. With this method the address information is more accuratse, because it relies on data that has been manually reviewed and verified. Therefore, it is possible that the addresses returned by the geolocation APIs are not as accurate the Places API.

For this case apart from the latitude and longitude, we will also use the hotel name returned by the Hotel Search API. That will make the request more specific to ensure that we will return one result only. 

At the coordinates `48.8682, 2.33395` there is a hotel called `HOTEL VILLA PANTHEON`.

#### Text Search API

For this example we will call the [Text Search API](https://developers.google.com/maps/documentation/places/web-service/search-text) which allows the search of a specific place or type of place (such as a hotel) using a string of text. The service responds with a list of places matching the text string and any location bias that has been set.

```python
import requests
import json

google_key = 'GOOGLE_API_KEY'
hotel_name = 'HOTEL VILLA PANTHEON'
lat_lng = '48.84917,2.34615'

base_url = 'https://maps.googleapis.com/maps/api/place/textsearch/json'
params = '?location=' + lat_lng + '&query=' + hotel_name + '&radius=10&key=' + google_key
url = base_url + params

headers = {
  'Accept': 'application/json'
}

response = requests.request('GET', url, headers=headers, data={})
json_response = json.loads(response.text)
print(json_response['results'][0]['formatted_address'])

```

#### Nearby Search API

You can also call the [Nearby Places API](https://developers.google.com/maps/documentation/places/web-service/search-nearby) to achieve the same functionality. This API allows you to search for places within a specified area around a set of coordinates.

```python
import requests
import json

google_key = 'GOOGLE_API_KEY'
hotel_name = 'HOTEL VILLA PANTHEON'
lat_lng = '48.84917,2.34615'

base_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
params = '?location=' + lat_lng + '&keyword=' + hotel_name + '&radius=10&key=' + google_key
url = base_url + params

headers = {
  'Accept': 'application/json'
}

response = requests.request('GET', url, headers=headers, data={})
json_response = json.loads(response.text)
print(json_response['results'][0]['vicinity'])
```

You can see the full code as well as the JSON response of all the searches in the GitHub repository.

In this tutorial we went through the methods of Reverse Geocoding and the Google Places API to translate a latitude and longitude location into a readable address in Python. By following the steps outlined in the tutorial, you will now be able to use these functionalities in your hotel applications. 