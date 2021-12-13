# -*- coding: utf-8 -*-
"""
Created on Wed Oct  9 22:38:18 2019

@author: Rahul Siyaynwal
         Dynamic Data Web Scraping, Saves all the links of headlines available in the economictimes website
"""

# -- Importing the libraries --
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import re
import time
from bs4 import BeautifulSoup
from tqdm import tqdm
import csv
import pandas as pd

# -- Importing the modules --
import src.web_config as config

# -- Setting up the chromedriver --
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome(config.CHROMEDRIVER, options=options)

# -- Getting the page source of the economictimes --
driver.get(config.ECONOMIC_TIMES)
page_source = driver.page_source
soup = BeautifulSoup(page_source, 'lxml')

links_list = []
for a in soup.find_all('a', href = True):
    print(a['href'])
    links_list.append(a['href'])
    
###############################################################################
# Cleaning the links acquired, creating a list of only inbound links  

new_list = []
for eachLink in links_list: 
    if re.match('^(http:\/\/|https:\/\/)(economictimes.indiatimes.com).*|^(\/).*', eachLink):
        new_list.append(eachLink)
        
# Adding domain prefix (Creating proper list of links)
string = config.ECONOMIC_TIMES_PREFIX
index_list = []
for mylist in new_list:
    if re.match('(^\/).*', mylist):
        index_list.append(string + mylist)
    else:
        index_list.append(mylist)
        
# List containing only archive links
archive_links = []
for s in index_list:
    if re.match('^(http:\/\/|https:\/\/)(economictimes.indiatimes.com/archive/).*', s):
        archive_links.append(s)
        
        
###############################################################################    
# Saving as CSV
# Creating a CSV file of inbound links

with open('Archive.csv', 'w') as f:
    writer = csv.writer(f)
    for val in archive_links:
        writer.writerow([val])

# -- Opening all URLs and geting the links in them --  
list_1 = []      
for all in tqdm(archive_links):
    driver.get(all)
    page_source = driver.page_source
    soup_all = BeautifulSoup(page_source, 'lxml')
    for a in soup_all.find_all('a', href = True):
        list_1.append(a['href'])
 
# -- Cleaning the urls (inbound only) --    
list_2 = []
for eachLink in list_1: 
    if re.match('^(http:\/\/|https:\/\/)(economictimes.indiatimes.com).*|^(\/).*', eachLink):
        list_2.append(eachLink)       

# -- Putting string at the start --
string = config.ECONOMIC_TIMES_PREFIX
list_3 = []
for mylist in list_2:
    if re.match('(^\/).*', mylist):
        list_3.append(string + mylist)
    else:
        list_3.append(mylist)

# -- List containing only archive links (till dates) --
archive_list_all = []
for s in tqdm(list_3):
    if re.match('^(http:\/\/|https:\/\/)(economictimes.indiatimes.com/archivelist/).*', s):
        archive_list_all.append(s)


# -- Saving all archive links --
with open(config.output + 'all-archive-links.csv', 'w') as f:
    writer = csv.writer(f)
    for val in archive_list_all:
        writer.writerow([val])
        
# -- Removing duplicates --
df = pd.read_csv(config.output + 'all-archive-links.csv')
df.drop_duplicates(subset = None, inplace = True)
df.to_csv('archive-link-lists.csv')

    
