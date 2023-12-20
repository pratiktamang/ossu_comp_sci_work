"""
Done
Welcome Pratik CF from Python for Everybody

Calling a JSON API

In this assignment you will write a Python program somewhat similar to http://www.py4e.com/code3/geojson.py.
The program will prompt for a location, contact a web service and retrieve JSON for the web service and parse that data,
and retrieve the first place_id from the JSON. A place ID is a textual identifier that uniquely identifies a place as within Google Maps.
API End Points

To complete this assignment, you should use this API endpoint that has a static subset of the Google Data:

http://py4e-data.dr-chuck.net/json?
This API uses the same parameter (address) as the Google API. This API also has no rate limit so you can test as often as you like.
If you visit the URL with no parameters, you get "No address..." response.
To call the API, you need to include a key= parameter and provide the address that you are requesting as the address= parameter that is
properly URL encoded using the urllib.parse.urlencode() function as shown in http://www.py4e.com/code3/geojson.py

Make sure to check that your code is using the API endpoint as shown above. You will get different results from the geojson and json endpoints
so make sure you are using the same end point as this autograder is using.

Test Data / Sample Execution

You can test to see if your program is working with a location of "South Federal University" which will have a place_id of "ChIJNeHD4p-540AR2Q0_ZjwmKJ8".

$ python3 solution.py
Enter location: South Federal University
Retrieving http://...
Retrieved 6052 characters
Place id ChIJNeHD4p-540AR2Q0_ZjwmKJ8
Turn In

Please run your program to find the place_id for this location:

University of Sarajevo
Make sure to enter the name and case exactly as above and enter the place_id and your Python code below. Hint: The first seven characters of the place_id are "ChIJAQA ..."
Make sure to retreive the data from the URL specified above and not the normal Google API. Your program should work with the Google API - but the place_id may not match for this assignment.

place_id: 
 
Python code:

"""


import urllib.request, urllib.parse, urllib.error
import json
import ssl

api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

if api_key is False:
    api_key = 42
    serviceurl = "http://py4e-data.dr-chuck.net/json?"
else:
    serviceurl = "https://maps.googleapis.com/maps/api/geocode/json?"

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

while True:
    address = input("Enter location: ")
    if len(address) < 1:
        break

    parms = dict()
    parms["address"] = address
    if api_key is not False:
        parms["key"] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print("Retrieving", url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print("Retrieved", len(data), "characters")

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or "status" not in js or js["status"] != "OK":
        print("==== Failure To Retrieve ====")
        print(data)
        continue

    # print(json.dumps(js, indent=4))
    print("place_id: ", js["results"][0]["place_id"])

    # lat = js["results"][0]["geometry"]["location"]["lat"]
    # lng = js["results"][0]["geometry"]["location"]["lng"]
    # print("lat", lat, "lng", lng)
    # location = js["results"][0]["formatted_address"]
    # print(location)


"""
 py calling_a_json_api.py                                                                                                                                                                2:39:21  ☁  main ☂ ✭
Enter location: University of Sarajevo
Retrieving http://py4e-data.dr-chuck.net/json?address=University+of+Sarajevo&key=42
Retrieved 3077 characters
{
    "results": [
        {
            "address_components": [
                {
                    "long_name": "8B",
                    "short_name": "8B",
                    "types": [
                        "street_number"
                    ]
                },
                {
                    "long_name": "Zmaja od Bosne",
                    "short_name": "Zmaja od Bosne",
                    "types": [
                        "route"
                    ]
                },
                {
                    "long_name": "Novo Sarajevo",
                    "short_name": "Novo Sarajevo",
                    "types": [
                        "political",
                        "sublocality",
                        "sublocality_level_1"
                    ]
                },
                {
                    "long_name": "Sarajevo",
                    "short_name": "Sarajevo",
                    "types": [
                        "locality",
                        "political"
                    ]
                },
                {
                    "long_name": "Kanton Sarajevo",
                    "short_name": "Kanton Sarajevo",
                    "types": [
                        "administrative_area_level_2",
                        "political"
                    ]
                },
                {
                    "long_name": "Federacija Bosne i Hercegovine",
                    "short_name": "Federacija Bosne i Hercegovine",
                    "types": [
                        "administrative_area_level_1",
                        "political"
                    ]
                },
                {
                    "long_name": "Bosnia and Herzegovina",
                    "short_name": "BA",
                    "types": [
                        "country",
                        "political"
                    ]
                },
                {
                    "long_name": "71000",
                    "short_name": "71000",
                    "types": [
                        "postal_code"
                    ]
                }
            ],
            "formatted_address": "Zmaja od Bosne 8B, Sarajevo 71000, Bosnia and Herzegovina",
            "geometry": {
                "location": {
                    "lat": 43.8563105,
                    "lng": 18.395895
                },
                "location_type": "ROOFTOP",
                "viewport": {
                    "northeast": {
                        "lat": 43.85765688029149,
                        "lng": 18.3973333802915
                    },
                    "southwest": {
                        "lat": 43.8549589197085,
                        "lng": 18.3946354197085
                    }
                }
            },
            "partial_match": true,
            "place_id": "ChIJAQAAsCPJWEcRn7nqFBP_ZYU",
            "plus_code": {
                "compound_code": "V94W+G9 Sarajevo, Bosnia and Herzegovina",
                "global_code": "8FMWV94W+G9"
            },
            "types": [
                "establishment",
                "point_of_interest",
                "university"
            ]
        }
    ],
    "status": "OK"
}
lat 43.8563105 lng 18.395895
Zmaja od Bosne 8B, Sarajevo 71000, Bosnia and Herzegovina
"""
