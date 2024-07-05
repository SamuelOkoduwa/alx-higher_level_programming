#!/usr/bin/python3
"""
This script fetches 10 most recent commits from a GitHub repository
and prints them in the format: <sha>: <author name>
"""

import requests
import sys

if __name__ == "__main__":
    repo_name = sys.argv[1]
    owner_name = sys.argv[2]

    url = f'https://api.github.com/repos/{owner_name}/{repo_name}/commits'
    params = {
        'per_page': 10  # Fetching 10 most recent commits
    }

    try:
        response = requests.get(url, params=params)
        commits = response.json()

        for commit in commits:
            sha = commit['sha']
            author_name = commit['commit']['author']['name']
            print(f"{sha}: {author_name}")
    
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data: {e}")

