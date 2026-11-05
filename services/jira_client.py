import requests
from requests.auth import HTTPBasicAuth
from config.config import JIRA_URL,EMAIL, API_TOKEN

def get_issue(issue_key):
    url = f"{JIRA_URL}/rest/api/3/issue/{issue_key}"
    response = requests.get(
        url, 
        auth=HTTPBasicAuth(EMAIL, API_TOKEN),
        headers={
            "accept":"application/json"
            }
        )
    
    print("Request URL:", url)
    print("Email:", EMAIL)
    print("STATUS:", response.status_code)
    print("RESPONSE:", response.text)

    return response.json()
    return response.json()