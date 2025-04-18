from meme_harvester import harvest_reddit
from twitter_scraper import scrape_twitter
from twitter_image_parser import extract_and_download
from meme_mutator import mutate_memes
from janus_instabot import post_mutated_memes

def main():
    print("🚀 Project Janus Key Activated")
    harvest_reddit()
    scrape_twitter()
    extract_and_download()
    mutate_memes()
    post_mutated_memes()

if __name__ == "__main__":
    main()
