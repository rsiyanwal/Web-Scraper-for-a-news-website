"""
Created on Sat Sept 26 14:10:15 2018
A code to create a csv file for the inbound links available on the Economic Times website.

Updated from October 07, 2019 onwards...

"""

#-- Importing the libraries --
import pandas as pd
import csv
import requests 
import re
from tqdm import tqdm
from bs4 import BeautifulSoup, SoupStrainer

# -- Importing the modules --
import src.web_config as config

#-- Link for Economic Times Archives --
domain = config.ECONOMIC_TIMES

#-- Getting Content --
content = requests.get(domain).content

"""
# Defining URL Formatting for links which doesn't have domain name at the start
string = 'https://economictimes.indiatimes.com'
def formatUrl(url):
    if re.match('[^https:\/\/economictimes.indiatimes.com].*', url):
        url = [string + url]
    return url
"""

###############################################################################
###### Getting all the links (may include outbound links) 
###### on the website mentioned above (domain)
###############################################################################    

links_list = []
soup = BeautifulSoup(content, "lxml")
print(soup.prettify())

for a in soup.find_all('a', href = True):
    print(a['href'])
    links_list.append(a['href'])

"""
for link in BeautifulSoup(content, parse_only=SoupStrainer('a')):
    print(link)
    if hasattr(link, 'href'):
        links_list.append(link)
"""

#-- Cleaning the links acquired, creating a list of only inbound links --  
new_list = []
length = links_list.__len__()

for eachLink in tqdm(links_list): 
    if re.match('^(http:\/\/|https:\/\/)(config.ECONOMIC_TIMES_TINY).*|^(\/).*', eachLink):
        new_list.append(eachLink)
        
#-- Adding domain prefix --
string = config.ECONOMIC_TIMES_PREFIX
index_list = []
for mylist in new_list:
    if re.match('(^\/).*', mylist):
        index_list.append(string + mylist)
    else:
        index_list.append(mylist)
        
        
###############################################################################    
#-- Creating a CSV file of inbound links --
with open(config.output + 'Archive_links.csv', 'w') as f:
    writer = csv.writer(f)
    for val in index_list:
        writer.writerow([val]) 
       
#-- Opening the links --
for linkks in links_list:
    if re.match('?!(^https:\/\/|http:\/\/)', linkks):
        link_content = requests.get(linkks).content
    
    
