# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 12:55:00 2019

@author: Rahul Siyanwal
         Content web scraping

"""
# Importing the libraries
import pandas as pd
import csv
import requests 
import re
from bs4 import BeautifulSoup, SoupStrainer
from tqdm import tqdm

# -- Importing modules --
import src.web_config as config

# -- Dynamic webdriver --
from selenium import webdriver
import time
options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--incognito')
options.add_argument('--headless')
driver = webdriver.Chrome("D:/chromedriver/chromedriver.exe", options=options)


# -- Reading the csv --
dataset = pd.read_csv(config.ARCHIVE_LINKS)
archive_list = dataset.squeeze().tolist()


# -- Getting content --
content_list = []
for s in tqdm(archive_list):
    driver.get(s)
    content = driver.page_source
    soup = BeautifulSoup(content, "lxml")
    """
    Edit this part to get other contents from the website. 
    The webscraper is scraping everthing available in webpage but we are 
    filtering only the headlines and dates.
    """
    getDate = []
    for a in soup.find_all(class_='contentbox5'):
        for b in a.find_all('b'):
            getDate.append(b.text)
        for c in a.find_all('a', href = True):
            #print(a.text)
            #getText.append(c.text)
            content_list.append((getDate[1],c.text,c['href']))
    
# -- Creating a CSV file of Headings --
with open('headings-economictimes.csv', 'w',newline='', encoding = 'utf-8') as f:
    writer = csv.writer(f)
    for val in content_list:
        writer.writerow(val)
