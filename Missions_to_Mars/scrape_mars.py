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
    hemisphere_image_urls = scrape_hemi_urls()
    facts_table_html = scrape_facts()
    return {"news_title": news_title, "news_text": news_p, "large_img_link": large_image_link, "hemi_urls": hemisphere_image_urls, "mars_facts": facts_table_html}
###############################

def scrape_image_otd():
    # Define url to scrape
    image_url = "https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars"
    browser.visit(image_url)

    # Click Full Size
    browser.click_link_by_partial_text('FULL IMAGE')

    # Splinter
    # Visit and parse web page
    html = browser.html
    soup = BeautifulSoup(html, "html.parser")
    
    #Find image element
    image_blob = soup.find("img", class_="fancybox-image")
    # Return just the src
    image_link = (image_blob['src'])
    #print(image_link)

    #The image link is the last record returned
    large_image_link = "http://www.jpl.nasa.gov" + image_link

    return large_image_link

def scrape_facts():
    # Mars Facts with pandas scraping
    # Set url
    url = "https://space-facts.com/mars/"
    factspage = pd.read_html(url)
    #print(type(factspage[1]))
    facts_table = factspage[1]

    # Set index to Mars - Earth Comparison
    facts_table.set_index("Mars - Earth Comparison", inplace=True)
    facts_table.head()
    facts_table = facts_table.drop(columns = ["Earth"])
    facts_table.head()
    facts_table_html = facts_table.to_html()

    #Convert facts_table to dictionary
    #facts_dictionary = facts_table.to_dict()
    #print(facts_dictionary)

    # Do I need to return anything here since I saved to html above
    return facts_table_html


def scrape_hemi_urls():
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

    # Create dictionary of image values
    # Create empty dict
    hemisphere_image_urls = [
        {"title": "Cerebus Hemisphere", "img_url": cerberus_link},
        {"title": "Schiaparelli Hemisphere", "img_url": schiaparelli_link},
        {"title": "Syrtis Major Hemisphere", "img_url": syrtis_link},
        {"title": "Valles Marineris Hemisphere", "img_url": valles_link}    
    ] 

    return hemisphere_image_urls