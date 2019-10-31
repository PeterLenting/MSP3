import os
from bson.json_util import dumps, loads
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import re

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'on_the_road'
app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor@myfirstcluster-sykdi.mongodb.net/on_the_road?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", additions=mongo.db.additions.find())

@app.route('/search')
def search():
    """Provides logic for search bar"""
    orig_query = request.args['query']
    # using regular expression setting option for any case
    query = {'$regex': re.compile('.*{}.*'.format(orig_query)), '$options': 'i'}
    # find instances of the entered word
    results = mongo.db.additions.find({
        '$or': [
            {'city': query},
        ]
    }).sort('current_date', -1)
    return render_template('search.html', query=orig_query, results=results)

@app.route('/addlocation')
def addlocation():
    return render_template("addlocation.html")


@app.route('/insert_location', methods=['POST'])
def insert_location():
    additions = mongo.db.additions
    additions.insert_one(request.form.to_dict())
    return redirect("get_index")


@app.route('/about')
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
