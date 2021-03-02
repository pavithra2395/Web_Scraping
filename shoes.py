import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import pandas

url = 'https://www.amazon.in/s?k=washing+machine+fully+automatic+top+load&crid=300TP8JJD86L8&sprefix=washing+machine%2Caps%2C309&ref=nb_sb_ss_ts-doa-p_3_15'
# driver = webdriver.Chrome(executable_path='chromedriver.exe')
# w = driver.get(url)
soup = requests.get(url)
web_page = BeautifulSoup(soup.content,features='html.parser')

s = web_page.find_all('div',attrs={'class':'a-section aok-relative s-image-fixed-height'})
images = []
for i in s:
    img = i.find('img')['src']
    images.append(img)
# print(len(images))
b = web_page.find_all('span',attrs={'class':'a-price-whole'})
prize = []
for i in b:
    prize.append(i.text)
# print(len(prize))
d = web_page.find_all('span',attrs={'class':'a-size-medium a-color-base a-text-normal'})
content = []
for i in d:
    content.append(i.text)
# print(content)

res = []
for i in range(len(images)):
    temp = {}
    temp['Image_url'] = images[i]
    temp['Content'] = content[i]
    temp['Prize'] = prize[i]
    res.append(temp)

print(res)
df = pandas.DataFrame.from_dict(res)
df.to_csv('washing.csv')









