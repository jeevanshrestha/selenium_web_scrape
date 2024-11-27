import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from  selenium.webdriver.chrome.options import Options
s = Service("C:/Users/jeevan.shrestha/Documents/chromedriver-win64/chromedriver.exe")
options = Options()
driver = webdriver.Chrome(service = s, options=options)
driver.get('https://www.ajio.com/men-backpacks/c/830201001')
time.sleep(1)

old_height = driver.execute_script('return document.body.scrollHeight')
counter = 0
while True:

    driver.execute_script('window.scrollTo(0 , document.body.scrollHeight)')
    time.sleep(2)
    new_height = driver.execute_script('return document.body.scrollHeight')

    counter += 1
    print(new_height)
    print(counter)
    if new_height == old_height:
        break

    old_height = new_height
# Wait for user input to close the browser

html = driver.page_source

with open('ajio_men_backpacks.html', 'w', encoding='utf-8') as f:
    f.write(html)
input("Press Enter to exit...")
driver.quit()
