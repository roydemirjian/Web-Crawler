import re 
import ssl
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Starting Page
seed = "https://en.wikipedia.org/wiki/NASA"

#Search term input by user
term = input('ENTER SEARCH TERM FOR [' + seed + ']: ')

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

#File to write to for relevant pages
f = open('relevant_urls.txt',"w")

#File to write to for all crawled pages
f2 = open('all_crawled_pages.txt',"w")

numberofterms = 0
#Iterate through list for matching results 
for items in urls:
        if '/wiki/' in str(items):
                #Write all crawled pages to file
                f2.write("https://en.wikipedia.org" + items)
                f2.write("\n")
        if term in str(items):
                #Write all relevant pages to file
                numberofterms += 1
                f.write("https://en.wikipedia.org" + items)
                f.write("\n")

#Close files
f.close()
f2.close()


#-----------------------------------------------------------
print("Starting Seed: " + seed)

print("Search Term: " + term)

print("Number of links found: " + str(numberoflinks))

print("Number of relevant links found (Using Terms): " + str(numberofterms))