from instagrapi import Client
import os
from dotenv import load_dotenv

def post_mutated_memes():
    load_dotenv()
    cl = Client()
    cl.login(os.getenv("IG_USERNAME"), os.getenv("IG_PASSWORD"))

    for file in os.listdir("memes/mutated"):
        if file.endswith((".jpg", ".jpeg", ".png")):
            cl.photo_upload(os.path.join("memes/mutated", file), "#JanusKey strikes again 🧠💥")
