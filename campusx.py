# open google.com
# search campusx
# learnwith.xampux.in
# dsmp course page
import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
s = Service("C:/Users/jeevan.shrestha/Documents/chromedriver-win64/chromedriver.exe")

driver = webdriver.Chrome(service = s)
driver.get('https://www.google.com')
time.sleep(2)

#fetch the search input using xpath
user_input = driver.find_element(by=By.XPATH, value='//*[@id="APjFqb"]')
user_input.send_keys('Campusx')
time.sleep(1)
user_input.send_keys(Keys.ENTER)

link = driver.find_element(by=By.XPATH, value='//*[@id="rso"]/div[1]/div/div/div/div/div/div/div/div[1]/div/span/a')
link.click()

time.sleep(1)

link2 = driver.find_element(by=By.XPATH, value='//*[@id="1698390585510d"]/div/div[1]/div/div/div/div[1]/div/div/div[2]/a[2]')
link2.click()

time.sleep(1)


# Wait for user input to close the browser
input("Press Enter to exit...")
driver.quit()