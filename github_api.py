# -*- coding: utf-8 -*-
"""github_API.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1pLPvF-geoe7kDoEI46yAjkXMU4oiJ9YP
"""

from github import Github

# token revoked for (now) obvious reasons
g = Github("8a16a8b561ff29e092a2c5767c8250725ebdfd19")

for repo in g.get_user().get_repos():
    print(repo.name)
    #repo.edit(has_wiki=False)
    # to see all the available attributes and methods
    print(dir(repo))

repo = g.get_repo("bitcoin/bitcoin")

print(repo.name)

repo2 = g.get_repo("stellar/stellar-core")

print(repo2.name)

print(repo.forks_count)

print(repo.stargazers_url)



