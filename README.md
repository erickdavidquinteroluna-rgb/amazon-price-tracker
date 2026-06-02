# Amazon Price Tracker

Python script that monitors Amazon product prices and sends email alerts when the price drops into your target range.

## Features
- Scrapes real-time prices from Amazon Mexico
- Checks price every hour automatically
- Sends email alert when price is within target range
- Configurable min/max target price

## Tech
Python · Selenium · BeautifulSoup · smtplib

## Usage
1. Set your email and app password in CONFIG
2. Set your target price range
3. Run `python3 price_tracker.py`
4. Paste any Amazon product URL
