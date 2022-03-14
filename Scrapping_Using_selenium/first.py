from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

PATH='C:\Program Files (x86)\chromedriver.exe'

driver = webdriver.Chrome(PATH)
driver.get("https://www.google.com")
print(driver.title) # gives the title of webpage
search = driver.find_element_by_name("q")
search.send_keys("Cricket")   # this means we want to search Cricket 
search.send_keys(Keys.RETURN) # here is says that after typing cricket I want to press Enter ( return == enter)

data_ved= driver.find_element_by_id('rso')
print(data_ved.text)

time.sleep(5)  # sleeping for 5 sec to visulaize the output
#driver.close() #It closes the tab
driver.quit() # closes the whole browser