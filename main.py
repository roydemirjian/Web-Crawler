import re 
import ssl
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Starting Page
seed = "https://en.wikipedia.org/wiki/NASA"

#Search term
term = 'space'

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
numberoflinks = 0
for links in title:
        urls.append(links.get('href'))
        numberoflinks += 1

#Open file 
f = open('crawled_urls.txt',"w")

numberofterms = 0
#Iterate through list for matching results 
for items in urls:
    if '/wiki/' in str(items):
        if term in str(items):
            numberofterms += 1
            #print("https://en.wikipedia.org" + items)
            f.write("https://en.wikipedia.org" + items)
            f.write("\n")

f.close()

print("NUMBER OF LINKS FOUND: " + str(numberoflinks))

print("NUMBER OF RELEVANT LINKS FOUND (USING TERMS): " + str(numberofterms))