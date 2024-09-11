import os
import requests
from dotenv import load_dotenv

load_dotenv()

GITHUB_NAME = os.getenv('GITHUB_NAME')
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
GITHUB_REP = os.getenv('GITHUB_REP')

URL = 'https://api.github.com/'


def create_repo(repo_name):
    url = f"{URL}/user/repos"
    response = requests.post(url, json={'name': repo_name, 'privite': False}, auth=(GITHUB_NAME, GITHUB_TOKEN))
    return response


def repo_exists(repo_name):
    url = f"{URL}/users/{GITHUB_NAME}/repos"
    response = requests.get(url, auth=(GITHUB_NAME, GITHUB_TOKEN))
    if response.status_code == 200:
        repos = response.json()
        return any(repo['name'] == repo_name for repo in repos)
    return False


def repo_delete(repo_name):
    url = f"{URL}/repos/{GITHUB_NAME}/{repo_name}"
    response = requests.delete(url, auth=(GITHUB_NAME, GITHUB_TOKEN))
    return response


if __name__ == "__main__":
    # Создаем репозиторий
    print(f"Creating repository '{GITHUB_REP}'...")
    create_response = create_repo(GITHUB_REP)

    if create_response.status_code == 201:
        print("Repository created successfully.")
    else:
        print(f"Failed to create repository: {create_response.json()}")

    # Проверяем наличие репозитория
    print(f"Checking if repository '{GITHUB_REP}' exists...")
    if repo_exists(GITHUB_REP):
        print("Repository exists.")
    else:
        print("Repository does not exist.")

    # Удаляем репозиторий
    print(f"Deleting repository '{GITHUB_REP}'...")
    delete_response = repo_delete(GITHUB_REP)

    if delete_response.status_code == 204:
        print("Repository deleted successfully.")
    else:
        print(f"Failed to delete repository: {delete_response.json()}")