import os
import requests
import random

PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
PAGE_ID = os.getenv("PAGE_ID")

quotes = [
    "🌟 Believe in yourself. You are unstoppable.",
    "🔥 Success comes from never giving up.",
    "💪 Work hard today for a better tomorrow.",
    "🚀 Your dreams are valid. Go get them!",
    "✨ Stay positive. Stay strong.",
]

message = random.choice(quotes)

url = f"https://graph.facebook.com/{PAGE_ID}/feed"
data = {
    "message": message,
    "access_token": PAGE_ACCESS_TOKEN
}

response = requests.post(url, data=data)
print(response.json())
