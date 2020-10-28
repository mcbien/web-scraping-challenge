from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
import scrape_mars
# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'

# Pass connection string to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
db = client.Mars_db

#Define index/home

# Define index/home route
@app.route('/scrape')
def scrape():
    
    mars_dictionary = scrape_mars.scrape()

    # PASTE ALL OF THE CELLS FROM THE WEB SCRAPE NOTEBOOK HERE

    # write values to mongo db:
        # Lastest Mars news:
            # news title   
            # news_p

        # Featured Mars Image
            # featured image url rendering image
            # Mars facts table >> mars_earth_facts table export

        # Mars Hemispheres
            # photogrid
            # Valles > Cerberus
            # Schiaparelli > Sytis Major


    # render the index page and provide our dictionary
    return render_template("index.html", mars_data=mars_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
