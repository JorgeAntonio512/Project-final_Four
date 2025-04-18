# Project final_Four 🧠🔥

## Overview
**Project final_Four** contains two operational sub-projects:

- **Project Janus Key** – Memetic destabilization of all cryptocurrencies except BTC, ETH, USDT, and XRP.
- **Project Princess** – Algorithmic trading augmentation to support the destruction of all other cryptocurrencies.

## Folder Structure

```
project_finalFour/
├── Project_Janus_Key/
│   ├── janus_key.py
│   ├── meme_harvester.py
│   ├── twitter_scraper.py
│   ├── twitter_image_parser.py
│   ├── meme_mutator.py
│   ├── janus_instabot.py
│   └── memes/
│       ├── harvested/
│       ├── mutated/
│       └── custom/
├── Project_Princess/
│   └── princess.py
```

## Setup Instructions

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root with your credentials:
```bash
cp .env.template .env
```

3. Run Janus Key or Princess:
```bash
cd project_finalFour/Project_Janus_Key
python janus_key.py

cd ../../Project_Princess
python princess.py
```

## Notes
- Instagram integration requires `instagrapi`
- Reddit scraper uses `praw`
- Twitter scraper uses `snscrape`

🔥 Strike while the iron's hot.
