import requests 
import apikey
import json

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer %s" % apikey.api_key
    }
params = {
    "location": "Leicester"
    }


response = requests.get(url,  params=params, headers=headers)
businesses = response.json()["businesses"]
# to get the name of each business from the list 
for business in businesses:
   print(business["name"])
# to get the name of a business rating that has above a 3.5 rating 
ratings = [business["name"] for business in businesses if business["rating"] > 3.5 ]
print(ratings)