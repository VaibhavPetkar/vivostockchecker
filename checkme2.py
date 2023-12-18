import requests
from bs4 import BeautifulSoup
import platform
import os
import time

# Function to fetch HTML content from a URL
def fetch_html(url):
    try:
        response = requests.get(url)
        return response.text
    except requests.RequestException as e:
        print("Error fetching HTML:", e)
        return None

# Function to search for data-lang-key="product.detail.buynow" in HTML and play beep sound
def search_and_play_beep(html_content):
    if html_content:
        soup = BeautifulSoup(html_content, 'html.parser')
        elements = soup.find_all(attrs={"data-lang-key": "product.detail.buynow"})

        if elements:
            # Play beep sound based on the operating system
            if platform.system() == "Windows":
                import winsound
                for i in range(0,20):
                    winsound.Beep(1000, 500)  # Change frequency and duration as needed
                    print("stock Open Buy Now")
            elif platform.system() == "Darwin":  # macOS
                os.system("afplay /path/to/beep-sound.mp3")  # Replace with your sound file path
            # Add support for Linux or other OS here if needed

# Get URL from the user
user_url = "https://shop.vivo.com/in/product/10254?skuId=18852"

# Fetch HTML content from the given URL


# Search for the specified attribute and play beep sound if found

while True:
    html_content = fetch_html(user_url)
    search_and_play_beep(html_content)
    print("Product is still out of stock.")
    time.sleep(60)  # Wait for 60 seconds before checking again (change as needed)