import requests
from bs4 import BeautifulSoup
import pandas

url = 'https://www.javatpoint.com/python-programs'

soup = requests.get(url)
# print(soup)
web_page = BeautifulSoup(soup.content,features="html.parser")
# print(web_page)
d = web_page.find_all('ul',attrs={'class':'points'})
d = d[0:len(d)-1]

print(len(d))

x = ['Basic Python programs','Python programs with conditions and loops', 'Python Function Programs', 'Python Native Data Type Programs','Python Array Programs','Python Number Programs','Python Circular Linked List Programs','Python Doubly Linked List Programs']


all = []
for item in x:
    dummy = item
    item = {}
    for i in d:
        li = i.find_all('a')
        links = []
        for link in li:
            # print(link['href'])
            links.append(link['href'])

        item[dummy] = links

    all.append(item)
# for i in all:
#     fw = open('kkk.txt','a')
#     fw.write(str(i)+'\n')
#     fw.close()
#
print(all)
# print(len(all))


#
df = pandas.DataFrame.from_dict(all)
df.to_csv('aaaa.csv')

