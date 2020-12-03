import requests
from bs4 import BeautifulSoup

response = requests.get("https://stackoverflow.com/questions")
soup = BeautifulSoup(response.text,"html.parser")
questions = soup.select(".question-summary")

#question[0] - first question
print(type(questions[0]))
print(questions[0].attrs)
#print the value of first question with the key - id
print(questions[0]["id"])
#first question
print(questions[0].select_one(".question-hyperlink").getText())

#all questions
for question in questions:
    print(question.select_one(".question-hyperlink").getText())
    # votes for each question
    print(question.select_one(".vote-count-post").getText())


