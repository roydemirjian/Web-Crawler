import re 
import ssl
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Starting Page
seed = "https://en.wikipedia.org/wiki/NASA"

#Get html
pageContent = urlopen(seed).read()

#Parse
soup = BeautifulSoup(pageContent, 'html.parser')

#Find links and append to list
titles = soup.find_all('a')
urls=[]
for link in titles:
    urls.append(link.get('href'))

#--------testing print---------
for items in urls:
    print(items)
