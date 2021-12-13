# Web-Scraper-for-a-news-website
This is a webscraper for a specific website (Economic Times). It is tuned to extract the headlines of that website. With some little adjustments the webscraper is able to extract any part of the website. 

# Installation
Install the following:
1. **Selenium:** Please follow the link https://selenium-python.readthedocs.io/installation.html and install the selenium.
2. **Chromedriver:** Check your Chrome browser's version (Menu -> Help -> About Google Chrome) and download the relevant Chromedriver from https://sites.google.com/chromium.org/driver/home
3. **TQDM:** https://pypi.org/project/tqdm/
4. **BeautifulSoup4:** https://pypi.org/project/beautifulsoup4/

# Using the webscraper
It is important to take care of the sequence of executing these files. Please follow the sequence below:
1. **ET_Archive_Links.py:** Use this website as it is the source of everything that we'll do later. This scripy gives us the initial links in the Archive page of the website. 
2. **ET_All_Links_Inside_Archive.py:** This is the script that takes the output (csv file) of the previous script. It produces a new file which contain URLs of all the archived news on the website since 2002. 
3. **ET_Content.py:** Finally, this is the script that scrapes the headlines along with the dates. *( If you want to scrap any other part of the website then this is the script that you have to edit )*

# Dataset
I used the scraper on another news website named "Businessline". It's dataset is available on Kaggle(https://www.kaggle.com/rsiyanwal/20182019-businessline-headlines).
