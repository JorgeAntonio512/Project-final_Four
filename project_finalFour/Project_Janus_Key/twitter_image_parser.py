import json
import os
import requests
from urllib.parse import urlparse

def extract_and_download():
    with open("memes/twitter_memes.json", 'r') as f:
        for line in f:
            tweet = json.loads(line)
            media = tweet.get('media', [])
            for item in media:
                if item['type'] == 'photo':
                    url = item['fullUrl']
                    filename = os.path.basename(urlparse(url).path)
                    filepath = os.path.join("memes/harvested", f"tw_{filename}")
                    if not os.path.exists(filepath):
                        r = requests.get(url)
                        with open(filepath, 'wb') as out:
                            out.write(r.content)
