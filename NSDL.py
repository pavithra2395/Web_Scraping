from selenium import webdriver
import os
import requests
import time
import sys
import urllib.request as uliib

from selenium.webdriver.common.by import By

print("Loading driver...")

# def NSDL():
driver = webdriver.Chrome(executable_path=r'D:\Users\rishi\WebScrapping\chromedriver')
driver.maximize_window()

url = 'https://nsdl.co.in/downloadables/list-debt.php'

driver.get(url)

time.sleep(10)

flag = False
link = []
# data = []

users = driver.find_elements(by=By.XPATH, value="/html/body/div[1]/div[2]/div[2]/div")
# d = {}
# name=""
for j, f in enumerate(users):
    if j > 7:

        cmp = f.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[2]/div[2]/div[{j}]")
        # print(cmp.text)
        # if cmp.text != "":
        #     name=cmp.text
        #     print(cmp.text)
        #     print("**************************")

        if cmp.get_attribute("class") == "language6":

            ul = cmp.find_element(by=By.XPATH, value=f"/html/body/div[1]/div[2]/div[2]/div[{j}]/div/ul")
            try:
                if ul.find_element(By.TAG_NAME, value="p") != None:
                    ele = ul.find_element(By.TAG_NAME, value="p").find_element(by=By.TAG_NAME, value="a")
                    # d.update({"link": ele.get_attribute('href'), "name": cmp.text})
                    link.append(ele.get_attribute('href'))
                    # data.append(d)
                    # name=""
            except:
                flag = True
                pass

            if flag:
                try:
                    if ul.find_element(By.TAG_NAME, value ="li") != None:
                        ele = ul.find_element(By.TAG_NAME, value ="li").find_element(by=By.TAG_NAME, value="a")
                        # d.update({"link": ele.get_attribute('href'), "name": cmp.text})
                        link.append(ele.get_attribute('href'))
                        # data.append(d)
                        # name=""
                except:
                    pass



#*********************************************Download the files**************************************************
def get_name(filename):
    if filename != '':
        name = os.path.basename(filename)
        print(name)
        return name


l_count = 0
# exc = ''
for l in link:
    print(l_count)
    fn=get_name(l.replace("%20", "_"))
    res = uliib.urlopen(l)

    with open(fr"D:\Users\rishi\WebScrapping\download\NSDL\{fn}", 'wb') as f:
        f.write(res.read())
        print(f"Succsess {l_count}")

    l_count += 1
    if l_count == len(link):
        break

    time.sleep(10)
# NSDL()