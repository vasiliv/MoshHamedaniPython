#https://www.dataquest.io/blog/web-scraping-tutorial-python/
import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")

#print(page) # <Response [200]> - means success
#print(page.status_code) # 200
#print(page.content) #html source of the page

soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify()) #html source of the page with nice layout
#1- 'html', 2 - '\n', 3 - <html><head><title>A simple example page</title></head><body><p>....

#print(list(soup.children)) #select all the elements at the top level of the page using the children property
#print([item for item in list(soup.children)])
#print([type(item) for item in list(soup.children)])

#We can now select the html tag and its children by taking the third item in the list:
#soup masivis me-3 cevris childreni. igives abrunebs rac html = list(soup)[2]
html = list(soup.children)[2]
#print(html)

#we can find the children inside the html tag:
#print(list(html.children))

#there are two tags here, head, and body.
# We want to extract the text inside the p tag, so we’ll dive into the body:
body = list(html.children)[3]
# print(body)

#get the p tag by finding the children of the body tag:
list(body.children)

#isolate the p tag:
p = list(body.children)[1]
#print(p)

#Once we’ve isolated the tag, we can use the get_text method to extract all of the text inside the tag:
#print(p.get_text())

#Finding all instances of a tag at once
#print(soup.find_all('p'))

#find_all returns a list, so we’ll have to loop through, or use list indexing, it to extract text:
#print(soup.find_all('p')[0].get_text())

#first instance of a tag, you can use the find method, which will return a single BeautifulSoup object:
#print(soup.find('p'))

#Searching for tags by class and id
page = requests.get("http://dataquestio.github.io/web-scraping-pages/ids_and_classes.html")
soup = BeautifulSoup(page.content, 'html.parser')
#print(soup.prettify())

#search for any p tag that has the class outer-text:
#print(soup.find_all('p', class_='outer-text'))

#any tag that has the class outer-text:
#print(soup.find_all(class_="outer-text"))

#search for elements by id:
#print(soup.find_all(id="first"))

#BeautifulSoup objects support searching a page via CSS selectors using the select method
print(soup.select("div p"))