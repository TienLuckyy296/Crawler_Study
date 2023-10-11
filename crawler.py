from bs4 import BeautifulSoup 
import requests 
# import sys
# import codecs
# sys.stdout = codecs.getwriter("utf-8")(sys.stdout, 'xmlcharrefreplace')
website = 'https://subslikescript.com/movie/Titanic-120338'
result = requests.get(website)
content = result.text 

soup = BeautifulSoup(content, 'lxml')
# print(soup.prettify())

box = soup.find('article', class_='main_article')
print(" ============ ")
print(box)
print(" ============ ")
title = box.find('h1').get_text()
# print(title)
transcript = box.find('div',class_='full-script').get_text(strip=True, separator=' ')
# print(transcript)
with open(f'{title}.txt', 'w', encoding='UTF-8') as file: 
    file.write(transcript)