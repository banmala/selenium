# from selenium import webdriver

# PATH="/home/banmala/Documents/chromedriver/chromedriver"
# driver=webdriver.Chrome(PATH)
# driver.get("https://www.facebook.com")
# print(driver.title)
# driver.quit()


#2nd tutorial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

PATH="/home/banmala/Documents/chromedriver/chromedriver"
driver=webdriver.Chrome(PATH)

driver.get("https://www.flipkart.com/")
print(driver.title)

# search =driver.find_element_by_name("email")
# search.send_keys("sunilbanmala0@gmail.com")

# search =driver.find_element_by_name("pass")
# search.send_keys("Mmylovemango0")

#search.send_keys(Keys.RETURN)

# driver.quit()
search =driver.find_element_by_name("q")
search.send_keys("Laptop")
search.send_keys(Keys.RETURN)
