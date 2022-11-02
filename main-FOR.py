import requests

project = input('Insira o nome do projeto:')
repo = input('Insira o nome do repositório:')
pr_state = 'open'
result = requests.get('https://api.github.com/repos/'+ project +'/'+ repo +'/pulls?state=' + pr_state)
json_result = result.json()

for i, value in enumerate(json_result):
    pagination_limit = 10
    if i < pagination_limit:
        print(value['title'] + ' - ' + value['url'])