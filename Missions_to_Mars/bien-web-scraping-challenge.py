#!/usr/bin/env python
# coding: utf-8

# ### Michael Bien: web-scraping-challenge

# In[33]:


# import dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup


# In[34]:


# Windows user
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)


# In[35]:


# Retreive page with request
#response = requests.get(url)


# In[36]:


# Create BeautifulSoup object
# soup = BeautifulSoup(response.text, 'html.parser')


# In[37]:


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
first_h = first_headline.find("div", class_="content_title")
news_title = first_h.text.strip()

article = soup.find("div", class_="article_teaser_body")
news_p = article.text.strip()

# Quit browser
#browser.quit()


# In[38]:


print(news_title)
print(news_p)


# In[39]:


# Define url to scrape
image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
browser.visit(image_url)

# Splinter
# Visit and parse web page
html = browser.html
soup = BeautifulSoup(html, "html.parser")

# Review soup object
#print(soup)


# In[40]:


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


# In[41]:


#The image link is the last record returned
large_image_link = "http://www.jpl.nasa.gov" + image_link[-1]
large_image_link


# In[42]:


# Mars Facts with pandas scraping
# Set url
url = "https://space-facts.com/mars/"
factspage = pd.read_html(url)
#print(type(factspage[1]))
facts_table = factspage[1]

# Quit browser
#browser.quit()


# In[43]:


# Set index to Mars - Earth Comparison
facts_table.set_index("Mars - Earth Comparison", inplace=True)
facts_table.head()


# In[44]:


# Convert dataframe to HTML
facts_table.to_html("mars_earth_facts")


# In[45]:


# ##ABANDONING THIS CELL AS IT IS NOT NECESSARY ##
# # Mars hemispheres
# # Set url to visit
# hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"
# browser.visit(hemi_url)

# # Splinter
# # Visit and parse web page
# html = browser.html
# soup = BeautifulSoup(html, "html.parser")
    
# #Beautiful Soup
# # Print first list item
# #first_headline = soup.find("li", class_="slide")

# link_titles = soup.find_all("a", class_="itemLink product-item")
# #len(link_titles)

# # Create empty list to collect link titles


# In[51]:


# Mars hemispheres images using splinter
# Set url to visit
hemi_url = "https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars"

#Browse to webpage
browser.visit(hemi_url)
# Use splinter to grab link
browser.click_link_by_partial_text('Cerberus')
#print(browser.find_by_text('Sample')['href'])
cerberus_link = browser.find_by_text('Sample')['href']

# #Browse to webpage
browser.visit(hemi_url)
# Use splinter to grab link
browser.click_link_by_partial_text('Schiaparelli')
#print(browser.find_by_text('Sample')['href'])
schiaparelli_link = browser.find_by_text('Sample')['href']

# #Browse to webpage
browser.visit(hemi_url)
# Use splinter to grab link
browser.click_link_by_partial_text('Syrtis')
#print(browser.find_by_text('Sample')['href'])
syrtis_link = browser.find_by_text('Sample')['href']

# #Browse to webpage
browser.visit(hemi_url)
# Use splinter to grab link
browser.click_link_by_partial_text('Valles')
#print(browser.find_by_text('Sample')['href'])
valles_link = browser.find_by_text('Sample')['href']

# Quit browser
browser.quit()

# print links
print(cerberus_link)
print(schiaparelli_link)
print(syrtis_link)
print(valles_link)


# In[53]:


# Create dictionary of image values
# Create empty dict
hemisphere_image_urls = [
    {"title": "Cerebus Hemisohere", "img_url": cerberus_link},
    {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_link},
    {"title": "Syrtis Major Hemisphere", "img_url": syrtis_link},
    {"title": "Valles Marineris Hemisphere", "img_url": valles_link}    
]


# In[54]:


print(hemisphere_image_urls)


# In[16]:


#Import additional dependencies
import pymongo
from pprint import pprint


# In[17]:


# Create connection to mongodb server
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)


# In[18]:


# Declare the db in Mongo
db = client.MarsDB
# Define collection
mars_collection = db.mars_material


# In[19]:


mars_collection.insert_one(
        


)


# In[ ]:





# In[ ]:





# In[ ]:




