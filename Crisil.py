from selenium import webdriver
import os
import requests
import time
import sys
import urllib.request as ul

print("Loading driver...")

def crisil():
    driver = webdriver.Chrome(executable_path=r'D:\Users\rishi\WebScrapping\chromedriver')
    driver.maximize_window()

    url = 'https://www.crisil.com/en/home/our-businesses/india-research/capital-market/crisil-market-linked-debenture-valuations.html'

    driver.get(url)

    time.sleep(1)

    print("--------Company list---------")
    users = driver.find_elements_by_class_name("normal-rte-list")
    link = []
    cmp_list = []
    print(len(users))
    d = 0
    for c, e in enumerate(users):
        # cmp_list.append(e.text)
        cmp_list = e.text.split('\n')
        # print(e.text.split('\n'))
        for a in e.find_elements_by_xpath('.//a'):
            print(f"{cmp_list[d]}")
            print(f"{a.get_attribute('href')}")
            link.append(a.get_attribute('href'))
            print("\n")
            d+=1

    #**************************************************************************************************
    l_count = 0
    # exc = ''
    for l in link:
        print(l_count)
        res = ul.urlopen(l)

        with open(r"D:\Users\rishi\WebScrapping\download\Crisil\{0}.pdf".format(cmp_list[l_count].replace(' ', '_')), 'wb') as f:
            f.write(res.read())
            print(f"Succsess {l_count}")

        l_count += 1
        if l_count == len(link):
            break

        time.sleep(10)

