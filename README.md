# web-scraping-challenge
Michael Bien web-scraping-challenge

This was a very challenging homework!!

Repository contains the following:

1. Jupyter Notebook: bien_web-scraping-challenge.ipynb -- contains all of the scraping
2. final screenshots folder: contain 3 screenshots of the final webpage
3. app.py: The flask app - calls the scraping from scrape_mars.py
4. scrape_mars.py: contains all of the scrape elements for the webpage
5. templates folder -- contains:
        a. index.html - the webpage template
        b. mars_earth_facts.html which is an unused file

Thanks to Matt for helping to iron out the final bug!!

General function:
1. Data is scrapped from various Nasa websites and displayed in the index.html file
2. Data is pwersistently written to MongoDB
    database: MarsDB
    collection: mars_data