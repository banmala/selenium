# from selenium import webdriver

# PATH="/home/banmala/Documents/chromedriver/chromedriver"
# driver=webdriver.Chrome(PATH)
# driver.get("https://www.facebook.com")
# print(driver.title)
# driver.quit()


# search =driver.find_element_by_name("email")
# search.send_keys("sunilbanmala0@gmail.com")

# search =driver.find_element_by_name("pass")
# search.send_keys("Mmylovemango0")

#search.send_keys(Keys.RETURN)

# driver.quit()


#2nd tutorial
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import requests as rq
from bs4 import BeautifulSoup as soup
import csv

searchh = input("What do you want to search:")

PATH="/home/banmala/Documents/chromedriver/chromedriver"
driver=webdriver.Chrome(PATH)


driver.get("https://www.flipkart.com/")
# print(driver.title)
 
search =driver.find_element_by_name("q")
search.send_keys(searchh)

search.send_keys(Keys.RETURN)

try:
    # main = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.CLASS, "t-0M7P _2doH3V"))
    # )
    # print(main)
    url = driver.current_url
    site_url=url+"&page={}"
    filename=searchh+".csv"
    f=open(filename,"w")
    headers="Product_Name,Features\n"
    f.write(headers)

    for i in range(1,11):
        site_url=site_url.format(i)
        site_html=rq.get(site_url).text
        html_content=soup(site_html,"lxml")

        containers=(html_content.findAll("div",{"class":"_1UoZlX"}))



        for container in containers:
            title=(container.findAll("div",{"class":"_3wU53n"})[0].text)
            
            con=(container.findAll("ul",{"class":"vFw0gD"})[0])
            features=[]
            for i in con:
                features.append((i.text))
            count=len(features)
            price=(container.findAll("div",{"class":"_1vC4OE _2rQ-NK"})[0].text.strip())
            try:
                rating=(container.findAll("div",{"class":"hGSR34"})[0].text)
            except:
                rating="0"
            #print(title.replace(",","|") + "," + features[0].replace(",","|") + "," + features[1].replace(",","|") + "," + features[2].replace(",","|") + "," + features[3].replace(",","|") + "," + features[4].replace(",","|") + "," + features[5].replace(",","|") + "," +  price.replace(",","") + "," + rating +"\n")
            f.write(title.replace(",","|") + ",")
            for i in range(count):
            	f.write(features[i].replace(",","|") + ",")
            f.write(price.replace(",","") + "," + rating +"\n")
    f.close()


    driver.quit()
except:
    driver.quit()


