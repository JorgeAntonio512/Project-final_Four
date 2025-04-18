import os
def scrape_twitter():
    query = "#cryptomeme OR #bitcoinmemes"
    os.system(f"snscrape --jsonl --max-results 30 twitter-search '{query}' > memes/twitter_memes.json")
