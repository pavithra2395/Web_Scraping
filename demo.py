from bs4 import BeautifulSoup
import requests
import pandas

# url = 'https://www.flipkart.com/watches/wrist-watches/pr?sid=r18%2Cf13&p%5B%5D=facets.brand%255B%255D%3DFastrack&p%5B%5D=facets.brand%255B%255D%3DCasio&p%5B%5D=facets.brand%255B%255D%3DFossil&p%5B%5D=facets.brand%255B%255D%3DSonata&p%5B%5D=facets.brand%255B%255D%3DTitan&p%5B%5D=facets.brand%255B%255D%3DDaniel%2BKlein&p%5B%5D=facets.brand%255B%255D%3DTimex&p%5B%5D=facets.brand%255B%255D%3DMaxima&p%5B%5D=facets.brand%255B%255D%3DDiesel&p%5B%5D=facets.brand%255B%255D%3DEmporio%2BArmani&p%5B%5D=facets.brand%255B%255D%3DU.%2BS.%2BPOLO%2BASSN.&p%5B%5D=facets.brand%255B%255D%3DArmani%2BExchange&p%5B%5D=facets.brand%255B%255D%3DTissot&p%5B%5D=facets.brand%255B%255D%3DTommy%2BHilfiger&p%5B%5D=facets.brand%255B%255D%3DSF&p%5B%5D=facets.brand%255B%255D%3DGuess&p%5B%5D=facets.brand%255B%255D%3DMichael%2BKors&p%5B%5D=facets.brand%255B%255D%3DFrench%2BConnection&p%5B%5D=facets.brand%255B%255D%3DTommy%2Bhilfiger&p%5B%5D=facets.brand%255B%255D%3DTed%2BBaker&p%5B%5D=facets.brand%255B%255D%3DScuderia%2BFerrari&p%5B%5D=facets.brand%255B%255D%3DLacoste&p%5B%5D=facets.brand%255B%255D%3DHugo%2BBoss&p%5B%5D=facets.brand%255B%255D%3DWROGN&p%5B%5D=facets.brand%255B%255D%3DVan%2BHeusen&p%5B%5D=facets.brand%255B%255D%3DImara&p%5B%5D=facets.brand%255B%255D%3DPeter%2BEngland&p%5B%5D=facets.brand%255B%255D%3DREEBOK&p%5B%5D=facets.brand%255B%255D%3DAllen%2BSolly&p%5B%5D=facets.brand%255B%255D%3DMetronaut&p%5B%5D=facets.brand%255B%255D%3DMarie%2BClaire&p%5B%5D=facets.brand%255B%255D%3DTED%2BBAKER&p%5B%5D=facets.price_range.from%3D1000&p%5B%5D=facets.price_range.to%3DMax&hpid=BPmMEaEpj3lGm0K0c0VD4qp7_Hsxr70nj65vMAAFKlc=&fm=neo%2Fmerchandising&iid=M_38c3c8d0-f475-4b86-ade1-ce0482101e8a_7.X4JO1628CDLI&ppt=browse&ppn=browse&ssid=me1ec4kz3k0000001614592762542&otracker=hp_omu_Today%2527s%2BFashion%2BDeals_4_7.dealCard.OMU_X4JO1628CDLI_6&otracker1=hp_omu_PINNED_neo%2Fmerchandising_Today%2527s%2BFashion%2BDeals_NA_dealCard_cc_4_NA_view-all_6&cid=X4JO1628CDLI'

url = 'https://www.amazon.in/deal/85a68c9e/ref=br_msw_pdt-2?_encoding=UTF8&smid=A14CZOWI0VEHLG&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_s=&pf_rd_r=EYEBPHVBVABRQ5M4FN3T&pf_rd_t=36701&pf_rd_p=5c669f94-aee5-4b22-81f8-1d301ca2c6a3&pf_rd_i=desktop'
soup = requests.get(url)

web_page = BeautifulSoup(soup.content)

d = web_page.find_all('img',attrs={'class':'octopus-dlp-asin-image'})

v = web_page.find_all('span',attrs={'class':'a-size-base a-color-base'})
v_1= []
for i in v:
    i = i.text
    i = i.strip()
    v_1.append(i)

p = web_page.find_all('span',attrs={'class':'a-price-whole'})

res = []
for i in range(len(d)):
    temp = {}
    temp['Name']= d[i]['src']
    temp['Title']=v_1[i]
    temp['Prize'] = p[i].text
    res.append(temp)

print(res)
df = pandas.DataFrame.from_dict(res)
df.to_csv('result5.csv')

