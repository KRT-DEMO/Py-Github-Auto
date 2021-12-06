import requests

GitHub_API = 'https://api.github.com/user/repos'
headers = {'Accept': 'application/vnd.github.v3+json'}
user = 'KRT-Demo'
password = 'Dog.Bone1'
personal_access_token = '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'

response = requests.get(GitHub_API, headers=headers, auth=(user, personal_access_token))

assert response.status_code == 200
print(response.status_code)
print(response.content)
