import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.tutorialspoint.com/python_pandas/python_pandas_dataframe.htm'
soup = requests.get(url)
# print(soup)
web_page = BeautifulSoup(soup.content, features="html.parser")
# print(web_page)
d = web_page.find_all('ul',attrs={'class':'toc chapters'})
# print(d)
# print(len(d))
topics = []
classes = []
for i in d:
    # print(i)
    name = i.find('a')['href']
    # print(name)
    classes.append(name)
    # print(i.text)
    topics.append(i.text)
    # print('*'*100)
# print(topics)

all = []
# print(classes)
for cls in classes:
    dummy = cls
    divs = web_page.find_all('div',attrs={'class':cls})
    for i in divs:
        cls = {}
        a = (i.select('li a'))
        links = []
        for link in a:
            links.append(link['href'])
        cls[dummy] = links

    all.append(cls)
print(all)

for i in all:
    fw = open('aa.txt','a')
    fw.write(str(i)+'\n')
    fw.close()