from selenium import webdriver
from selenium.webdriver.safari.service import Service
from bs4 import BeautifulSoup
import time
import smtplib
from email.mime.text import MIMEText

# ── CONFIG ──────────────────────────────
EMAIL = "put your email here"
APP_PASSWORD = "put your app password here"  # tu clave de 16 caracteres
TARGET_MIN = 500.0
TARGET_MAX = 600.0
CHECK_EVERY = 3600  # revisa cada hora (en segundos)
# ────────────────────────────────────────

def get_price(url):
    driver = webdriver.Safari()
    driver.get(url)
    time.sleep(3)
    soup = BeautifulSoup(driver.page_source, "html.parser")
    driver.quit()
    price = soup.find("span", {"class": lambda c: c and "a-price-whole" in c})
    if price:
        raw = price.text.replace(",", "").replace(".", "").strip()
        return float(raw)
    return None

def send_alert(price, url):
    msg = MIMEText(f"Price alert!\n\nCurrent price: ${price}\nTarget range: ${TARGET_MIN} - ${TARGET_MAX}\n\nBuy now: {url}")
    msg["Subject"] = f"Amazon Alert: ${price} is within your target!"
    msg["From"] = EMAIL
    msg["To"] = EMAIL
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, APP_PASSWORD)
        server.send_message(msg)
    print("Email sent!")

url = input("Paste Amazon URL: ").strip()

while True:
    price = get_price(url)
    if price:
        print(f"Current price: ${price} | Target: ${TARGET_MIN}-${TARGET_MAX}")
        if TARGET_MIN <= price <= TARGET_MAX:
            send_alert(price, url)
    time.sleep(CHECK_EVERY)