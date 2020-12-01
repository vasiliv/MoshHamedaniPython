#Мэтиз - Изучаем Python_ программирование игр, визуализация данных, веб-приложения (2020)
import requests
# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'

#avkripot es url chromeshi da .R inspect. Network tab - Headers tab
#da Request Header-shi aris Accept
#Accept: text/html,application/xhtml+xml,application/xml;
#q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9

#headers mean HTTP headers:

headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# headers examples: 'date', 'content-type', 'server', 'status' ...
r1 = requests.get(url)
print("HEADERS!!!")
print(r1.headers)

# Сохранение ответа API в переменной.
response_dict = r.json()
# Обработка результатов.
print("response_dict.keys()!!!")
print(response_dict.keys())

#выводится значение, связанное с 'total_count', которое представляет
#общее количество репозиториев Python в GitHub
print(f"Total repositories: {response_dict['total_count']}")
# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Анализ первого репозитория.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)

print("\nSelected information about first repository:")
print(f"Name: {repo_dict['name']}")
print(f"Owner: {repo_dict['owner']['login']}")
print(f"Stars: {repo_dict['stargazers_count']}")
print(f"Repository: {repo_dict['html_url']}")