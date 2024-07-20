#!/usr/bin/env python
# coding: utf-8

# In[1]:


import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver


# In[127]:


def quote_scraper(pagedata):
    x = pagedata.find_all("div","quotes")
    y = x[0].find_all("div","quote")
    
    regex = re.compile("[^a-zA-Z '.]+")

    quotes = []
    authors = []

    for quote in y:
        text = quote.find("div","quoteText").get_text()
        text = text.strip()
        text = regex.sub('',text)
        author = quote.find("span","authorOrTitle").get_text()
        author = author.strip()
        author = author.replace(",","")
        author = regex.sub('',author)
        text = text.split(author)
        text = text[0]
        text = text.strip()
        quotes.append(text)
        authors.append(author)
    
    dict = {"Quote":quotes,"Author":authors}
    df = pd.DataFrame.from_dict(dict)
        
    return df


# In[131]:


if __name__ == "__main__":
    
    appended_data = []
    
    driver = webdriver.Chrome(r"C:\Users\250202\OneDrive - NTT DATA Group\Conrad Harker\chromedriver.exe")
    
    for page in range(1,101):
        driver.get(f'https://www.goodreads.com/quotes?page={page}')
        time.sleep(2)
        pagedata = BeautifulSoup(driver.page_source, "html.parser")
        df = quote_scraper(pagedata)
        appended_data.append(df)
        
    driver.quit()
    
    df_main = pd.concat(appended_data)


# In[132]:


df_main


# In[133]:


df_main.to_csv("C:\Users\harke\OneDrive\Desktop\Python\quotes\input\quotes_x.csv", index=False)

