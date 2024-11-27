import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
s = Service("C:/Users/jeevan.shrestha/Documents/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service=s)

driver.get('https://www.catch.com.au/event/black-friday-sale-185091/')
time.sleep(1)



old_height = driver.execute_script('return document.body.scrollHeight')
while True:

    try:
        driver.find_element(by=By.XPATH, value='/html/body/main/div[3]/article/footer/div/a').click()
        time.sleep(3)

        new_height = driver.execute_script('return document.body.scrollHeight')

        print(old_height)
        print(new_height)

        if new_height == old_height:
            break

        old_height = new_height
    except ElementClickInterceptedException as e:
        print("Element not clickable.")
        break
    except Exception as e:
        print(e)
        break

html = driver.page_source

with open('catch-black-friday.html','w',encoding='utf-8') as f:
    f.write(html)

# Wait for user input to close the browser
input("Press Enter to exit...")
driver.quit()