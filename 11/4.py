import requests

url = "https://api.yelp.com/v3/businesses/search"
api_key = "9U6JEI8h2sQJhoFOhziygMqut83kMjoFWYr5lT0XO9IoqH1euWMGJ8e479rkQxio_sDltjCJVSefMRmMcF0QiB2fMUTyAAQKqLDv0_fZjHBkchPs8kw2ezVaoeHEX3Yx"
#dictionary (key-value pairs)
headers = {
    "Authorization:", "Bearer " + api_key
}
response = requests.get(url, headers=headers)
print(response)