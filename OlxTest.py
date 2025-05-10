import sys
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Fix UnicodeEncodeError in Windows terminal
sys.stdout.reconfigure(encoding='utf-8')

# Setup Chrome options
options = Options()
# DO NOT USE HEADLESS MODE — OLX may block it
options.add_argument("start-maximized")
options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"
)

# Start the Chrome driver
driver = webdriver.Chrome(options=options)
driver.get("https://www.olx.in/items/q-car-cover")

# Let the page load
print(" Waiting for OLX page to load...")
time.sleep(10)

# Scroll slowly to load more listings
print(" Scrolling to load listings...")
for _ in range(10):
    driver.execute_script("window.scrollBy(0, 1000);")
    time.sleep(2)

# Get listing items
items = driver.find_elements(By.CSS_SELECTOR, 'li[data-aut-id="itemBox"]')
print(f" Listings found: {len(items)}")

# Extract title, price, and location
results = []
for item in items:
    try:
        title = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemTitle"]').text.strip()
        price = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="itemPrice"]').text.strip()
        location = item.find_element(By.CSS_SELECTOR, 'span[data-aut-id="item-location"]').text.strip()
        results.append(f"{title} | {price} | {location}")
    except Exception:
        continue

driver.quit()

# Save to file
with open("olx_car_covers.txt", "w", encoding="utf-8") as f:
    for line in results:
        f.write(line + "\n")

print(" Results saved to olx_car_covers.txt")
