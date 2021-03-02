import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas

url = 'https://www.amazon.in/b?node=22430932031&pf_rd_r=9W0ETZ3Z6B9JBPZ3DTTT&pf_rd_p=75bfbb29-1102-448b-aa55-4becd89244c2&pd_rd_r=ec8ee9be-70e7-45a6-be06-0001a54e9533&pd_rd_w=hYbK3&pd_rd_wg=3kuHH&ref_=pd_gw_unk'

soup = requests.get(url)
# print(soup)
web_page = BeautifulSoup(soup.content)
# print(web_page)
s = web_page.find_all('div',attrs={'class':'acs-product-block__empty-badge'})
print(s)
print(len(s))
d = web_page.find_all('span',attrs={'class':'a-price-whole'})
print(d)
print(len(s))
e = web_page.find_all('span',attrs={'class':'a-truncate-full'})
# print(e)
print(len(e))
