import requests
from pytest_check import equal
import uuid
import json

BASE_GitHub_API_URL = 'https://api.github.com'
user_repos_route = '/user/repos'
headers = {"accept": "application/vnd.github.v3+json"}
user = 'KRT-Demo'
password = 'Dog.Bone1'
personal_access_token = ''
#--html=report.html --self-contained-html

def test_get_user_repos():
    response = requests.get(BASE_GitHub_API_URL + user_repos_route, headers=headers, auth=(user, personal_access_token))

    print(response.status_code)
    print(response.content)
    equal(response.status_code, 200)
    equal(response.status_code, 200)


def test_get_user_repos_2():
    response = requests.get(BASE_GitHub_API_URL + user_repos_route, headers=headers, auth=(user, personal_access_token))

    print(response.status_code)
    print(response.content)
    assert response.status_code == 200


def test_create_repo():
    payload = {
        'name': 'Repo ' + uuid.uuid4().hex,
        'description': uuid.uuid4().hex,
        'homepage': 'https://github.com',
        'private': False,
        'has_issues': True,
        'has_projects': True,
        'has_wiki': True,
        'is_template': False,
        'auto_init': True,
        'gitignore_template': 'Python',
        'license_template': 'mit',
        'allow_squash_merge': True,
        'allow_merge_commit': True,
        'allow_rebase_merge': True
    }
    response = requests.post(BASE_GitHub_API_URL + user_repos_route, headers=headers, auth=(user, personal_access_token), data=json.dumps(payload))

    print(response.status_code)
    print(response.content)
    assert response.status_code == 201



