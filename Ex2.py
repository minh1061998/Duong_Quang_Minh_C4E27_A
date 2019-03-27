from pymongo import MongoClient

mongo_uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"
client = MongoClient(mongo_uri)

Ex2 = client.c4e
comment2 = Ex2["customers"]

event = 0
wom = 0
ads =0

count = list(comment2.find())
# print(count)
for customer in count:
    if customer["ref"] == "events":
        event += 1
    elif customer["ref"] == "wom":
        wom +=1
    else:
        ads +=1   

print("events = ",event)
print("wom = ",wom)
print("ads = ",ads)

# Pie chart
from matplotlib import pyplot

ref_type = [event,wom,ads]
ref_name = ["events", "wom", "ads"]

pyplot.pie(ref_type, labels = ref_name, autopct="%.1f%%", explode =[0,0,0])
pyplot.axis("equal")
pyplot.title("Customers of a marketing")
pyplot.show()