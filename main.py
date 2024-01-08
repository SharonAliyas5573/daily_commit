import requests
from base64 import b64encode
from datetime import datetime, timezone, timedelta
import sys

# Replace with your GitHub credentials and repository details
owner = 'SharonAliyas5573'
repo = 'daily_commit'
path = 'update.txt'

token = sys.argv[1]

api_url = f'https://api.github.com/repos/{owner}/{repo}/contents/{path}'
headers = {
    'Authorization': f'Bearer {token}',
    'Accept': 'application/vnd.github.v3+json',
}

response = requests.get(api_url, headers=headers)
file_info = response.json()

sha = file_info['sha']
ist = timezone(timedelta(hours=5, minutes=30))
current_time_ist = datetime.now(ist).strftime('%Y-%m-%d %H:%M:%S')

content = f"Latest update {current_time_ist}"
content_base64 = b64encode(content.encode('utf-8')).decode('utf-8')  

# Prepare data for the request
data = {
    'message': 'repo updatted',
    'content': content_base64,
    'sha': sha,
}

# Make the request
response = requests.put(api_url, headers=headers, json=data)

