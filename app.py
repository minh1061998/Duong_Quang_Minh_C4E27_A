from flask import *
from services import Services
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["SECRET_KEY"] = "Anh bảnh bị bắt rồi ông giáo ạ"



@app.route('/')
def index():
    return render_template('hompage.html')

@app.route("/all-service")
def allservice():
  if "logged" in session:
    if session["logged"] == True:
      persons = Services.find()
      return render_template("all-service.html", all_persons = persons)
    else:
      return redirect("/login")
  else:
    return redirect("/login")

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

@app.route("/all-service/update/<id>", methods=["GET","POST"])
def update(id):
  update_person = Services.find_one({"_id": ObjectId(id)})
  if request.method =="GET":
# Get information

    return render_template("update.html",update = update_person)
  elif request.method == "POST":
    form = request.form
    services_name = form["input_Name"]
    services_age = form["input_Age"]
    services_gender = form["input_Gender"]
    services_height = form["input_Height"]
    services_address = form["input_Address"]
    services_available = form["input_Available"]

    new_value = {
      "$set":{
        "name": services_name,
        "age": services_age,
        "gender": services_gender,
        "height": services_height,
        "address": services_address,
        "available": services_available,
      }
    }
    Services.update_one(update_person, new_value)
    return redirect("/all-service/detail/{}".format(id))

@app.route("/login", methods = ["GET","POST"])
def login():
  if session["logged"]:
    return redirect("/all-service")
  else:  
    if request.method == "GET":  
      return render_template("Login.html")
    elif request.method == "POST":
      username = "admin" 
      password = "admin" 
      form = request.form 
      input_username = form["input_username"]
      input_password = form["input_password"]

      if input_username == username and input_password == password:
        session["logged"] = True
        return redirect("/all-service")
      else: 
        return redirect ("/login")

@app.route("/logout")
def logout():
  if "logged" in session:
    session["logged"] = False
    return redirect("/login")


if __name__ == '__main__':
  app.run( debug=True)
 