import re
import ssl
import os
from bs4 import BeautifulSoup
from urllib.request import urlopen

#Set up SSL environment
try:
    _create_unverified_https_context = ssl._create_default_https_context
except AttributeError:
    pass
else: 
    ssl._create_default_https_context = _create_unverified_https_context

#Get page content
def get_page_content(url):
    try:   
        html_response_text = urlopen(url).read()
        page_content = html_response_text.decode('utf-8')
        return page_content
    except Exception as e:
        return None

soup = BeautifulSoup(page_content,'html.parser')
page_text = soup.get_text()
title = soup.title.string
title = clean_title(title)

#Clean the title of a page
def clean_title(title):
    invalid_characters = ['<','>',':','"','/','\\','|','?','*']
    for c in invalid_characters:
        title = title.replace(c,'')
    return title

#Check if term is included in page text
if re.search(term, page_text, re.I):

#Extract inner urls from page content
def get_urls(soup):
    links = soup.find_all('a') 
    urls=[] 
    for link in links:
        urls.append(link.get('href'))
    return urls

#Check if url is valid
def is_url_valid(url):
    if url is None:
        return False
    if re.search('#', url):
        return False
    match = re.search('^/wiki/', url)
    if match:
        return True
    else:
        return False

#Reformat relative in full url
def reformat_url(url):
    match = re.search('^/wiki/',url)
    if match:
        return "https://en.wikipedia.org"+url
    else:
        return url

#Save page
def save(text,path)
    f = open(path,'w', encoding = 'utf-8', errors = 'ignore')
    f.write(text)
    f.close()

#Save crawled urls
f = open("crawled_urls.txt","w")
i = 1
for url in crawled_urls:
    f.write(str(i) + ': ' + url + '\n')
    i += 1
f.close()
