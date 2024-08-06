import requests
from bs4 import BeautifulSoup

website= "https://toscrape.com/"
result=requests.get(website)

content= result.text
soup= BeautifulSoup(content,'lxml')

box = soup.find('div',class_='container')
title = box.find('h1').get_text()
subtitle= box.find('h2').get_text()
text = box.find('p').get_text(strip=True, separator=' ')

print(subtitle)

