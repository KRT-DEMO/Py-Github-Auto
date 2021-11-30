import requests

GitHub_API = 'https://api.github.com'
User_Repos_Resource = '/user/repos'
headers = {'Accept': 'application/vnd.github.v3+json'}
#bearertoken = '3f275dd3fa9803072dd1299175f1e10079d0124a'
bearertoken = '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'

response = requests.get(GitHub_API, headers=headers, auth=('Authorization', bearertoken))

print(response.status_code)
print(response.content)