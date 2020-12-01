#Python Requests Tutorial: Request Web Pages, Download Images, POST Data, Read JSON, and More
#by Corey Schafer

import requests

response = requests.get("https://xkcd.com/353/")
#<Response [200]> means success
#print(response)
#all availeble attributes and methods of response object
#print(dir(response))

#html of a given page
#print(response.text)

# response_1 = requests.get("https://xkcd.com/comics/python.png")
# print(response)
# print(response_1.headers)

#https://httpbin.org is created specially for requests library
# payload_2 = {"page": 2,"count": 25}
# response_2 = requests.get("https://httpbin.org/get", params=payload_2)
# print(response_2.text)
# print(response_2.url)

# payload_3 = {"username":"corey", "password":"testing"}
# response_3 = requests.post("https://httpbin.org/post", data=payload_3)
# print(response_3.text)
#
# r_dict = response_3.json()
#accessing form dictionary
# print(r_dict["form"])

#corey is username, 1 - pass
# response_4 = requests.get("http://httpbin.org/basic-auth/corey/1",auth = ("corey","1"))
# print(response_4.text)
# print(response_4)

#shegnebuli shecdoma avtorizaciashi
# response_5 = requests.get("http://httpbin.org/basic-auth/corey/1",auth = ("corey","12"))
# print(response_5.text)
# print(response_5)

response_6 = requests.get("http://httpbin.org/delay/1",timout=3)
print(response_6)