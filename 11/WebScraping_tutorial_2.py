#https://www.dataquest.io/blog/web-scraping-tutorial-python/
import requests
from bs4 import BeautifulSoup

#Download the web page containing the forecast.
# Create a BeautifulSoup class to parse the page.
# Find the div with id seven-day-forecast, and assign to seven_day
# Inside seven_day, find each individual forecast item.
# Extract and print the first forecast item.

page = requests.get("http://forecast.weather.gov/MapClick.php?lat=37.7772&lon=-122.4168")
soup = BeautifulSoup(page.content, 'html.parser')
seven_day = soup.find(id="seven-day-forecast")
forecast_items = seven_day.find_all(class_="tombstone-container")
tonight = forecast_items[0]
#print(tonight.prettify())

period = tonight.find(class_="period-name").get_text()
short_desc = tonight.find(class_="short-desc").get_text()
temp = tonight.find(class_="temp").get_text()
print(period)
print(short_desc)
print(temp)

img = tonight.find("img")
desc = img['title']
print(desc)

#Select all items with the class period-name inside an item with the class tombstone-container in seven_day.
#Use a list comprehension to call the get_text method on each BeautifulSoup object.
period_tags = seven_day.select(".tombstone-container .period-name")
periods = [pt.get_text() for pt in period_tags]
print(periods)