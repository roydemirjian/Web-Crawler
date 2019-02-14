import re 
import ssl
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Starting Page
seed = "https://en.wikipedia.org/wiki/NASA"

#Get html
htmlResponse = urlopen(seed).read()
pageContent = htmlResponse.decode('utf-8')

#Parse
soup = BeautifulSoup(pageContent, 'html.parser')
title = soup.title.string

#Clean
def clean_title(title):
    invalid_characters = ['<','>',':','"','/','\\','|','?','*']
    for c in invalid_characters:
        title = title.replace(c,'')
    return title

title = clean_title(title)

#Find links and append to list
title = soup.find_all('a')
urls=[]
for links in title:
        urls.append(links.get('href'))

#------------testing---------------

#------------end testing ------------------

f = open('crawled_urls.txt',"w")

#Print
for items in urls:
    if '/wiki/' in str(items):
        print("https://en.wikipedia.org" + items)
        f.write("https://en.wikipedia.org" + items)
        f.write("\n")

f.close()