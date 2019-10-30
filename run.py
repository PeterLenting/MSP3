import os
from bson.json_util import dumps, loads
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myTestDB'
#app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor@myfirstcluster-sykdi.mongodb.net/task_manager?retryWrites=true&w=majority'
app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor@myfirstcluster-sykdi.mongodb.net/myTestDB?retryWrites=true&w=majority'

mongo = PyMongo(app)

'''
@app.route('/')
@app.route('/get_index')
def get_index():
    experiences=mongo.db.myFirstMDB.find()
    return render_template("index.html", index=loads(dumps(experiences)))
'''
@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", myFirstMDB=mongo.db.myFirstMDB.find())


@app.route('/addlocation')
def addlocation():
    return render_template("addlocation.html")


@app.route('/insert_location', methods=['POST'])
def insert_location():
    myFirstMDB = mongo.db.myFirstMDB
    myFirstMDB.insert_one(request.form.to_dict())
    return redirect("get_index")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
