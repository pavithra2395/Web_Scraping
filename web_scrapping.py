import requests
from bs4 import BeautifulSoup
import pandas


url = 'https://www.flipkart.com/search?q=laptop&sid=6bo%2Cb5g&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_3_na_na_na&as-pos=1&as-type=RECENT&suggestionId=laptop%7CLaptops&requestId=552f630f-53f0-40c5-b1a5-97351cf86620&as-backfill=on'

soup = requests.get(url)

web_page = BeautifulSoup(soup.content)

d = web_page.find_all('ul',attrs={'class':'_1xgFaf'})
laptops = web_page.find_all('div',attrs={'class':'_4rR01T'})

laptopnames = []
for i in laptops:
    laptopnames.append(i.text)

prizes = web_page.find_all('div',attrs={'class':'_30jeq3 _1_WHN1'})
all_prizes = []
for i in prizes:
    print(i.text)
    all_prizes.append(i.text)


content = []
for i in d:
    li_all = i.select('li')
    dummy = []
    for li in li_all:

        dummy.append(li.text)

    content.append(dummy)



print(len(laptopnames))
print(len(all_prizes))
print(len(content))

res = []
for i in range(len(all_prizes)):
    temp = {}
    temp['name']= laptopnames[i]
    temp['prize']= all_prizes[i]
    temp['content']= content[i]
    res.append(temp)


df = pandas.DataFrame.from_dict(res)
df.to_excel('result2.xlsx')
