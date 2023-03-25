import time
from selenium import webdriver

url = "https://github.com/anupzpt"

driver = webdriver.Chrome()

driver.get(url)

while True:
    driver.refresh()
    time.sleep(0.0001)
