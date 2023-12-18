import requests
from bs4 import BeautifulSoup
import platform
import os
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
# Function to fetch HTML content from a URL
sender_email = 'rajvaibhavpetkar007@gmail.com'  # Replace with your email
receiver_email = ['pranavmaniyar5555@gmail.com','vaibhavprakashpetkar@gmail.com']  # Replace with recipient email
subject = 'Mobile Stock On'

smtp_server = 'smtp.gmail.com'
smtp_port = 587  # TLS Port
server = smtplib.SMTP(smtp_server, smtp_port)
t=True

def sendmail():
    
    
    try:
        email_username = 'rajvaibhavpetkar007@gmail.com'  # Replace with your email
        email_password = 'aejaiqfugbzlucio'  # Replace with your password or app-specific password
        print(server.starttls())
        print(server.login(email_username, email_password))
        server.sendmail(sender_email, receiver_email, subject)
        print("Email sent successfully!")
    except:
         print("Error to send")

# Create a MIME object to represent the email


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
                print("stock Open Buy Now")
               
                for i in range(0,5):
                    sendmail()
                time.sleep(60*10)
                    
                
        
# Get URL from the user
user_url = "https://shop.vivo.com/in/product/10254?skuId=18852"

# Fetch HTML content from the given URL


# Search for the specified attribute and play beep sound if found

while True:
    html_content = fetch_html(user_url)
    search_and_play_beep(html_content)
    print("Product is still out of stock.")
    time.sleep(60)  # Wait for 60 seconds before checking again (change as needed)