import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.geeksforgeeks.org/python-programming-examples/'

soup = requests.get(url)
# print(soup)
web_page = BeautifulSoup(soup.content)
# print(web_page)
d = web_page.find_all('h2')


# print(d)
topics = []
classes = []
for i in d:
    # print(i)
    name = i.find('a')['name']
    # print(name)
    classes.append(name)
    # print(i.text)
    topics.append(i.text)
    # print('*'*100)
# print(topics)
all = []
# print(classes)

all = []
# print(classes)
for cls in classes:
    dummy = cls
    divs = web_page.find_all('div',attrs={'class':cls})
    if cls=='regex':
        continue

    else:
        for i in divs:
            cls = {}
            a = (i.select('li a'))
            links = []
            for link in a:
                links.append(link['href'])
            cls[dummy] = links


    all.append(cls)

# for i in all:
#     fw = open('kk.txt','a')
#     fw.write(str(i)+'\n')
#     fw.close()
#


# df = pandas.DataFrame.from_dict(all)
# df.to_csv('aaaa.csv')
