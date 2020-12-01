#https://realpython.com/python-requests/
import requests

# response = requests.get('https://api.github.com')
# print(response)
# #payload-poleznie dannie
# print(response.content)
# #payload in string format
# print(response.text)
#
# print(response.headers, end="\n")

response = requests.get(
    'https://api.github.com/search/repositories',
    params={'q': 'requests+language:python'},
    headers={'Accept': 'application/vnd.github.v3.text-match+json'},
)

# View the new `text-matches` array which provides information
# about your search term within the results
json_response = response.json()
repository = json_response['items'][0]
print(f'Text matches: {repository["text_matches"]}')
