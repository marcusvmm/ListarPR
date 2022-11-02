import requests

project = input('Insira o nome do projeto:')
repo = input('Insira o nome do repositório:')
pr_state = 'open'
per_page = '10'
result = requests.get('https://api.github.com/repos/'+ project +'/'+ repo +'/pulls?state=' + pr_state +'&per_page='+ per_page)
json_result = result.json()

for value in (json_result):
    print(value['title']+' - '+value['url'])
