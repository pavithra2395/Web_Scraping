# from selenium import webdriver
import os
import requests
import time
from selenium import webdriver

import urllib.request as ul
print("Loading driver...")

def icraanalytics():
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(executable_path=r'D:\Users\rishi\WebScrapping\chromedriver.exe', options=options)
    # wait = WebDriverWait(driver, 20)
    # driver.maximize_window()

    url = 'https://icraanalytics.com/Home/MldValuation#!#divMlddDetails'

    driver.get(url)

    time.sleep(1)

    print("--------Company list---------")

    page = []
    pages = driver.find_element_by_xpath("/html/body/div[1]/section[2]/div/div[2]/div/section/cl-paging/div")
    # pages = wait.until(EC.presence_of_element_located((By.CLASS_NAME,"md-ripple-container"))).find_element_by_xpath('//*[@id="divMlddDetails"]/div/section/cl-paging/div/button[3]').click()
    # print(type(pages))
    page = pages.text.replace('<', '').replace('>', '').strip().split('\n')
    print(len(page))


    lst = []
    table = driver.find_element_by_tag_name("table")
    lst = table.text.strip().split('\n')
    print(lst)

    # link = []
    # links = driver.find_element_by_xpath('.//a')
    # link.append(a.get_attribute('href'))
    # print(f"{a.get_attribute('href')}")
    link = []
    cmp_list = []
    a = None

    k = 0
    a=[]
    for i in range(len(page)):
        print(f"page : {i}")
        driver.find_element_by_xpath(f'//*[@id="divMlddDetails"]/div/section/cl-paging/div/button[{i + 3}]').click()

        for j in range(len(lst) - 1):
            tr = table.find_elements_by_xpath(f'/html/body/div[1]/section[2]/div/div[2]/div/div/table/tbody/tr[{j + 1}]/td[1]')
            value = tr[0].text.strip().split('\n')[0]
            # if value == '':
            cmp_list.append(value)

            a = table.find_elements_by_xpath(f'/html/body/div[1]/section[2]/div/div[2]/div/div/table/tbody/tr[{j + 1}]/td[3]/a')

            print(cmp_list[k])
            print(f"{a[0].get_attribute('href')}")
            print('\n')

            link.append(a[0].get_attribute('href'))
            k += 1

    # print(cmp_list)

    #**************************************************************************************************
    l_count = 0
    # exc = ''
    for l in link:
        print(f'download...{cmp_list[l_count]}')
        res = ul.urlopen(l)
        time.sleep(10)
        with open(r"D:\Users\rishi\WebScrapping\download\IcraAnalytics\{0}.pdf".format(cmp_list[l_count].replace(' ', '_')), 'wb') as f:
            f.write(res.read())
            print(f"Succsess {l_count}")

        l_count += 1
        if l_count == len(link):
            break

        time.sleep(10)