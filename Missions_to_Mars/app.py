from flask import Flask, render_template

# Import our pymongo library, which lets us connect our Flask app to our Mongo database.
import pymongo
from pprint import pprint
import scrape_mars
# Create an instance of our Flask app.
app = Flask(__name__)

# Create variable for our connection string
conn = 'mongodb://localhost:27017'

# Pass connection string to the pymongo instance.
client = pymongo.MongoClient(conn)

# Connect to a database. 
db = client.Mars_db

#### write scrapped data to MongDB
# connect to mongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)

# define MarsDB database in Mongo
db = client.MarsDB

# declare collection
collection = db.mars_data

#Define index/home
@app.route('/')
def index():
    return "Please visit /scrape route to see Mars info"


# Define index/home route
@app.route('/scrape')
def scrape():
    
    mars_dictionary = scrape_mars.scrape()

    

    # insert mars dictionary into database
    collection.insert_one(mars_dictionary)

    results = collection.find(mars_dictionary)
    for result in results:
        pprint(result)

    # render the index page and provide our dictionary
    return render_template("index.html", mars_data=mars_dictionary)


if __name__ == "__main__":
    app.run(debug=True)
