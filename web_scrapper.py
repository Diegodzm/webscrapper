import requests
from bs4 import BeautifulSoup

website= "https://toscrape.com/"
result=requests.get(website)

content= result.text
soup= BeautifulSoup(content,'lxml')

box = soup.find('div',class_='container')
title = box.find('h1').get_text()
transcript = box.find('div',class_='row').get_text(strip=True, separator=' ')
print(title,transcript)

with open(f'{title}.txt','w') as file:
    file.write(transcript)