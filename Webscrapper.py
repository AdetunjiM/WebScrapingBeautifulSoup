from codecs import utf_8_encode
from bs4 import BeautifulSoup
import requests
from csv import writer

fname="housing.csv"
url2= "http://www.google.com"
ursl = "https://www.airbnb.com/s/Indianapolis--IN/homes?adults=2&place_id=ChIJA2p5p_9Qa4gRfOq5QPadjtY&checkin=2022-11-13&checkout=2022-11-30"
url = "https://www.pararius.com/apartments/amsterdam?ac=1"
page = requests.get(url)

soup = BeautifulSoup(page.content,'html.parser')

lists = soup.find_all('section',class_="listing-search-item")

with open(fname,'w',encoding="utf8", newline='') as f:
    thewriter=writer(f)
    header=["Title","Location","Price","Area"]
    thewriter.writerow(header)
    for list in lists:
        title = list.find('a',class_="listing-search-item__link--title").text.replace('\n','')
        location = list.find('div',class_="listing-search-item__sub-title").text.replace('\n','')
        price = list.find('div',class_="listing-search-item__price").text.replace('\n','')
        area = list.find('li',class_="illustrated-features__item--surface-area").text.replace('\n','')
        info=[title,location,price,area]
        thewriter.writerow(info)

    