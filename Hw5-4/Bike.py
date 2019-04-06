from flask import *
from database import bike_colection
from bson.objectid import ObjectId

app = Flask(__name__)


# @app.route('/')
# def index():
#     return render_template('index.html')

@app.route("/new_bike", methods = ["GET","POST"])
def new_bike():
    if request.method == "GET":
        return render_template("Bike.html")
    elif request.method == "POST":
        form = request.form
        bike_Model = form["input_Model"]
        bike_Dailyfee = form["input_Dailyfee"]
        bike_Image = form["input_Image"]
        bike_Year = form["input_Year"]

        print(form)

        bike_document ={
            "Model": bike_Model,
            "Daily fee (VND)": bike_Dailyfee,
            "Image": bike_Image,
            "Year": bike_Year,
        }
        bike_colection.insert_one(bike_document)
        return redirect("/new_bike")

if __name__ == '__main__':
  app.run(debug=True)
 

