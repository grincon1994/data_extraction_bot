from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import requests
import re
import time

form_link = "https://docs.google.com/forms/d/e/1FAIpQLSe8HZhkj8H8ILlO3UqOA9zgSQLaI-yQaRNX6cabNpL9q9xorQ/viewform?usp=sf_link"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(chrome_options)
driver.get(form_link)

zillow_clone = "https://appbrewery.github.io/Zillow-Clone/"

home_links = []
home_prices = []
home_address = []

response = requests.get(zillow_clone)
soup = BeautifulSoup(response.content, 'html.parser')

links = soup.find_all('a')
prices = soup.find_all('span')
addresses = soup.find_all('address')


for link in links:
    href = link.get('href')
    if href and 'zillow' in href:
        home_links.append(href)

for price in prices:
    list_prices_text = price.get_text().strip()
    if '$' in list_prices_text:
        home_prices.append(list_prices_text.strip('+ /mo'))

for address in addresses:
    address_text = address.get_text().strip()
    if address_text:
        address_parts = address_text.split(',')[1:]  # Skip the first part
        clean_address = ','.join(part.strip() for part in address_parts).replace('|', '')
        home_address.append(clean_address)


#Filling Google Form

address_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
address_form.send_keys("hola")

time.sleep(2)

monthly_price_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
monthly_price_form.send_keys("nena")

time.sleep(2)

property_link_form = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
property_link_form.send_keys("bro")
# print(home_links)
# print(home_prices)
# print(home_address)
driver.quit()