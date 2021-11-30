import requests

GitHub_API = 'https://api.github.com/user/repos'
headers = {'Accept': 'application/vnd.github.v3+json'}
user = 'KRT-Demo'
personal_access_token = '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'

response = requests.get(GitHub_API, headers=headers, auth=(user, personal_access_token))

assert response.status_code == 200
print(response.status_code)
print(response.content)
