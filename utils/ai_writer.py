import requests
import json


# 目标 API 的 URL
url = "http://192.168.0.106:8000/api/article"

def write_article():
    data = {
        "title": "ai title",
        "body": "ai content",
        "type": "mdx",
        "tags": ['tag1', 'tag2'],
        "auth": {
            "username": 'admin',
        },
    }
    response = requests.post(
        url, 
        data=json.dumps(data),
        headers={
            "Content-Type": "application/json",
            "Accept": 'application/json',
        }
    )
    print("response:", response.json())

write_article()