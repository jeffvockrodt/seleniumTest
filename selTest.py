from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options

import time

options = Options()
options.headless = False
if options.headless:
    print ("Headless Firefox Initialized.")
    driver = webdriver.Firefox(options=options)
    url = 'https://ped.uspto.gov/peds/#!/'
    driver.get(url)
else:
    print("Firefox opened in normal (non-headless) mode.")
    driver = webdriver.Firefox()
    url = 'https://ped.uspto.gov/peds/#!/'
    driver.get(url)
time.sleep(2)

driver.get_screenshot_as_file('test.png')
print(driver.page_source)


driver.close()

