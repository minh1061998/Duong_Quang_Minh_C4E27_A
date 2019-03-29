from flask import *
from services import Services
from bson.objectid import ObjectId

app = Flask(__name__)



@app.route('/')
def index():
    return render_template('hompage.html')

@app.route("/all-service")
def allservice():
  persons = Services.find()
  return render_template("all-service.html", all_persons = persons)

@app.route("/all-service/detail/<id>")
def detail(id):
  detail_person = Services.find_one({"_id": ObjectId(id)})
  return render_template("details.html", detail_person = detail_person)

@app.route("/all-service/<g>")
def gender(g):
  services = Services.find({"gender": g})
  return render_template("all-service.html", all_persons = services)  

@app.route("/all-service/delete/<id>")  
def delete(id):
  delete_person = Services.find_one({"_id": ObjectId(id)})
  Services.delete_one(delete_person)
  return redirect("/all-service")
if __name__ == '__main__':
  app.run( debug=True)
 