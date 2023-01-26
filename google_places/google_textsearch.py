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
