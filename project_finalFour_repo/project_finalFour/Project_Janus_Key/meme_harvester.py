import praw
import requests
import os
from urllib.parse import urlparse

reddit = praw.Reddit(client_id="YOUR_CLIENT_ID",
                     client_secret="YOUR_CLIENT_SECRET",
                     user_agent="janus_key_meme_bot/0.1")

def harvest_reddit():
    subreddits = ["cryptomemes", "buttcoin", "cryptocurrency"]
    output_dir = "memes/harvested"
    os.makedirs(output_dir, exist_ok=True)

    for sub in subreddits:
        for post in reddit.subreddit(sub).hot(limit=10):
            if post.url.endswith(('.jpg', '.jpeg', '.png')):
                filename = os.path.basename(urlparse(post.url).path)
                filepath = os.path.join(output_dir, f"reddit_{filename}")
                if not os.path.exists(filepath):
                    r = requests.get(post.url)
                    with open(filepath, "wb") as f:
                        f.write(r.content)
