import requests
from pytest_check import equal
import uuid
import json
from approvaltests.approvals import verify

BASE_GitHub_API_URL = 'https://api.github.com'
user_repos_route = '/user/repos'
repos_route = '/repos'
user_route = '/user'
headers = {"accept": "application/vnd.github.v3+json"}
user = 'KRT-Demo'
password = 'Dog.Bone1'
personal_access_token = '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'


# Command Line argument to run pytest with html reports:
# pytest --html=report.html --self-contained-html

def test_get_user_repos():
    response = requests.get(BASE_GitHub_API_URL + user_repos_route, headers=headers, auth=(user, personal_access_token))

    print(response.status_code)
    print(response.content)
    # using pytest-checks allows errors allow validations to fail but still allow the test to run
    equal(response.status_code, 201)
    equal(response.status_code, 200)


def test_get_user_repos_2():
    response = requests.get(BASE_GitHub_API_URL + user_repos_route, headers=headers, auth=(user, personal_access_token))

    print(response.status_code)
    print(response.content)
    assert response.status_code == 200


def test_create_repo():
    payload = {
        'name': 'Repo_' + uuid.uuid4().hex,
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
    response = requests.post(BASE_GitHub_API_URL + user_repos_route, headers=headers,
                             auth=(user, personal_access_token), data=json.dumps(payload))

    print(response.status_code)
    print(response.content)
    assert response.status_code == 201


def test_delete_repo():
    payload = {
        'name': 'Repo_' + uuid.uuid4().hex,
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
    repo_name = payload['name']
    response = requests.post(BASE_GitHub_API_URL + user_repos_route, headers=headers,
                             auth=(user, personal_access_token), data=json.dumps(payload))

    assert response.status_code == 201

    # Delete repo that was created
    delete_response = requests.delete(BASE_GitHub_API_URL + repos_route + '/' + user + '/' + repo_name, headers=headers,
                                      auth=(user, personal_access_token))
    assert delete_response.status_code == 204

    get_response = requests.get(BASE_GitHub_API_URL + repos_route + '/' + user + '/' + repo_name, headers=headers,
                                auth=(user, personal_access_token))
    assert get_response.status_code == 404


def test_get_user_json_comparison_approval_test():
    response = requests.get(BASE_GitHub_API_URL + user_route, headers=headers,
                             auth=(user, personal_access_token))

    assert response.status_code == 200
    data = response.json()
    data.pop('public_repos')
    data.pop('disk_usage')
    data.pop('updated_at')
    jsonResult = json.dumps(data, indent=4)
    print(jsonResult)
    verify(jsonResult)
