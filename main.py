from pprint import pprint
import requests
from github import Github

username = 'G3nt1'
access_token = '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'
url = f"https://api.github.com/users/{username}"
user_data = requests.get(url).json()

pprint(user_data)

g = Github()
user = g.get_user(username)
for repo in user.get_repos():
    stars_count = repo.stargazers_count
    print(f"Repository: {repo.name}, Stars: {stars_count}")

