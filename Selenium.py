#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import urllib.request
from selenium import webdriver
import selenium.webdriver.common.keys


# ### The below function search_by_keyword() will allow user to enter a keyword and search for a specific image related to keyword on Google Images.

# In[2]:


def search_by_keyword():
    keyword=input("Enter a keyword:")
    driver = webdriver.Chrome("C:\\Users\\Admin\\Downloads\\chromedriver.exe")
    url=driver.get("https://www.google.com/imghp")
    driver.find_element_by_name("q").send_keys(keyword)
    driver.find_element_by_name("q").send_keys(u'\ue007')
    


# In[6]:


search_by_keyword()


# ### The below function download_image(url), takes image url as a parameter. Once you are done with search_by_keyword(), choose any image you wish to download and copy its image url and pass the url to download_image() function.

# In[4]:


def download_image(url):    
    name=random.randrange(1,5000)
    full_name=str(name)+".jpg"
    urllib.request.urlretrieve(url,full_name)

