# modules to interact with mongoDB
import pymongo # runs on 27017
import requests
# from bs4 import beautifulSoup as bs
# Import Libraries
import numpy as np

from flask import(
    Flask,
    render_template,
    jsonify,
    request)

#------------------------------------------------------------------------------------#
# Flask Setup #
#------------------------------------------------------------------------------------#
app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn)

# create / Use database
db = client.State

# look up State / document in the collection

db.Category
# iterate all States
# print("test1")
i = 1
for perState in db.State.find():
    if ('StateName' in perState and 'Counties' in perState):
        # print(perState['StateName'])
        # print(perState['Year'])
        for county in perState['Counties']:
            # print(county)
            i += 1
# print(i)

# Home Page --> Render Landing.html from template
@app.route("/")
def home():
    return(render_template("Landing.html"))

@app.route("/names")
def names():
    print("Names invoked")
    # Get the sample list which is the column names in Samples table 
    sample_list = []
    # First element in the samples_column_list is 'otu_id' so sample list is from 2nd element to the last element
    db = client.Category
    for item in db.Category.find():
        # print("inside find cat")
        if ('cat' in item):
            for cat in item['cat']:
                print(cat)
                sample_list.append(cat)
    # print(sample_list)
    return jsonify(sample_list)

#------------------------------------------------------------------------------------#
# Initiate Flask app
#------------------------------------------------------------------------------------#
if __name__=="__main__":
    connect_args={'check_same_thread':False}
    app.run(debug=True)