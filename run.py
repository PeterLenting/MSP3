import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'myTestDB.myFirstMDB'
app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor@myfirstcluster-sykdi.mongodb.net/task_manager?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", index=mongo.db.myFirstMDB.find())

@app.route('/addlocation')
def addlocation():
    return render_template("addlocation.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
