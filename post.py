import os
import requests

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

MESSAGE = "Hello! This is an automated Facebook post from my bot!"

url = f"https://graph.facebook.com/{PAGE_ID}/feed"
data = {
    "message": MESSAGE,
    "access_token": PAGE_ACCESS_TOKEN
}

response = requests.post(url, data=data)
print(response.json())
