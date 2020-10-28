#!/usr/bin/env python
# coding: utf-8

# ### Michael Bien: web-scraping-challenge

# In[115]:


# import dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup


# In[116]:


# Windows user
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[117]:


# Retreive page with request
#response = requests.get(url)


# In[118]:


# Create BeautifulSoup object
# soup = BeautifulSoup(response.text, 'html.parser')


# In[119]:


# Headline and article
# Define url to scrape
url = "https://mars.nasa.gov/news/"
browser.visit(url)

# Splinter
# Visit and parse web page
html = browser.html
soup = BeautifulSoup(html, "html.parser")
    
#Beautiful Soup
# Print first list item
first_headline = soup.find("li", class_="slide")
news_title = first_headline.h3.text.strip()

article = soup.find("div", class_="article_teaser_body")
news_p = article.text.strip()

# Quit browser
#browser.quit()


# In[120]:


print(news_title)
print(news_p)


# In[121]:


# Define url to scrape
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)

# Splinter
# Visit and parse web page
html = browser.html
soup = BeautifulSoup(html, "html.parser")

# Review soup object
#print(soup)


# In[122]:


# Click Full Size
#browser.click_link_by_partial_text('FULL IMAGE')
    
#Beautiful Soup
a_fancybox = soup.find_all("a", class_="fancybox")

# Print result
#print(a_fancybox)

# Create empty list to capture link
image_link = []
# Loop through results to find href
for box in a_fancybox:
      link = box['data-fancybox-href']
      image_link.append(link)

# print image link list
#image_link

# Quit browser
#browser.quit()


# In[123]:


#The image link is the last record returned
large_image_link = "http://www.jpl.nasa.gov" + image_link[-1]
large_image_link


# In[124]:


# Mars Facts with pandas scraping
# Set url
url = "https://space-facts.com/mars/"
factspage = pd.read_html(url)
#print(type(factspage[1]))
facts_table = factspage[1]

# Quit browser
#browser.quit()


# In[125]:


# Set index to Mars - Earth Comparison
facts_table.set_index("Mars - Earth Comparison", inplace=True)
facts_table.head()


# In[126]:


# Convert dataframe to HTML
facts_table.to_html("mars_earth_facts")


# In[82]:


# Mars hemispheres
# Set url to visit
hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"


#Browse to webpage
browser.visit(hemi_url)

browser.click_link_by_partial_text('Cerberus')
print(browser.find_by_text('Sample')['href'])

html = browser.html
soup = BeautifulSoup(html, "html.parser")

# Quit browser
# browser.quit()

#print(soup)


# In[76]:


# Examine soup object
a_tags = soup.find_all("a", href=True)
#print([link for link in a_tags if "enhanced.tif" in link])
print(a_tags)


# In[ ]:


##  FINISH THIS PART


# In[104]:


#Import additional dependencies
import pymongo
from pprint import pprint


# In[105]:


# Create connection to mongodb server
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[107]:


# Declare the db in Mongo
db = client.MarsDB
# Define collection
mars_collection = db.mars_material


# In[ ]:


mars_collection.insert_one(
        


)


# In[ ]:





# In[ ]:





# In[ ]:




