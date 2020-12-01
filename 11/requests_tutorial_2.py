#Мэтиз - Изучаем Python_ программирование игр, визуализация данных, веб-приложения (2020)
import requests
# Создание вызова API и сохранение ответа.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# Сохранение ответа API в переменной.
response_dict = r.json()
# Обработка результатов.
print(response_dict.keys())

print(f"Total repositories: {response_dict['total_count']}")
# Анализ информации о репозиториях.
repo_dicts = response_dict['items']
print(f"Repositories returned: {len(repo_dicts)}")
# Анализ первого репозитория.
repo_dict = repo_dicts[0]
print(f"\nKeys: {len(repo_dict)}")
for key in sorted(repo_dict.keys()):
    print(key)