from flask import Flask, render_template
from mlab import demo_collection
from pymongo import MongoClient
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route("/ex5/ex6")
def ex6():
    all_continent2 = demo_collection.find()
    return render_template("Ex6.html", continents2 = all_continent2)    



if __name__ == '__main__':
  app.run( debug=True)
 