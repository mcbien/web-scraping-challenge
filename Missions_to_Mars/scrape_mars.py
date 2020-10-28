# import dependencies
import pandas as pd
from splinter import Browser
from bs4 import BeautifulSoup

# Windows user
executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path, headless=False)

def scrape_news():
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
    # Print first list item
    first_headline = soup.find("li", class_="slide")
    first_h = first_headline.find("div", class_="content_title")
    news_title = first_h.text.strip()

    article = soup.find("div", class_="article_teaser_body")
    news_p = article.text.strip()

    return news_title, news_p


#### MAIN SCRAPE FUNCTION ####
def scrape():
    news_title, news_p = scrape_news()
    large_image_link = scrape_image_otd()
    return {"news_title": news_title, "news_text": news_p, "large_img_link": large_image_link}

def scrape_image_otd():
    # Define url to scrape
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    # Splinter
    # Visit and parse web page
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")

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

    #The image link is the last record returned
    large_image_link = "http://www.jpl.nasa.gov" + image_link[-1]
    large_image_link

    return large_image_link