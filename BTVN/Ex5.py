from pymongo import MongoClient
from mlab import demo_collection
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/ex5")
def Ex5():
    all_continent = demo_collection.find()
    return render_template("Ex5.html", continents = all_continent)


if __name__ == '__main__':
  app.run( debug=True)
 

