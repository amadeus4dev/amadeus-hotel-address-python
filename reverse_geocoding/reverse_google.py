import geocoder

lat_lng = [48.84917,2.34615]
response = geocoder.google(lat_lng, method='reverse')

print(response.json['address'])