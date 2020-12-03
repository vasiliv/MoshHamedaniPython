#https://www.w3resource.com/python-exercises/web-scraping/index.php
#Write a Python program to extract h1 tag from example.com

import requests
from bs4 import BeautifulSoup

url = "http://example.com/"
page = requests.get(url, "html.parser")
#print(page.status_code)
soup = BeautifulSoup(page.content, 'html.parser')
print(soup.find_all('h1'))

