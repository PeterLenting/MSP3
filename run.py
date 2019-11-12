import os
from bson.json_util import dumps, loads
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo
from bson.objectid import ObjectId

app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'on_the_road'
app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor@myfirstcluster-sykdi.mongodb.net/on_the_road?retryWrites=true&w=majority'

mongo = PyMongo(app)


@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", additions=mongo.db.additions.find())


@app.route('/add_addition')
def add_addition():
    categories = mongo.db.categories.find().sort('category_part', 1)
    chapters = mongo.db.chapters.find().sort('chapter', 1)
    return render_template('addaddition.html',  categories=categories, chapters=chapters)


@app.route('/insert_location', methods=['POST'])
def insert_location():
    additions = mongo.db.additions

    # get the value and convert it into an interger
    value = int(request.form.get('chapter_in_book'))
    value2 = int(request.form.get('part_of_book'))

    # Generate the fields and insert
    additions.insert_one(
        {
            'city': request.form.get('city'),
            'chapter_in_book': value,
            'location': request.form.get('location'),
            'date': request.form.get('date'),
            'part_of_book': value2,
            'quote_in_book': request.form.get('quote_in_book'),
            'name_visitor': request.form.get('name_visitor'),
            'experience': request.form.get('experience'),
        }
    )
    return render_template("index.html", additions=mongo.db.additions.find())


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/delete_addition/<addition_id>')
def delete_addition(addition_id):
    additions = mongo.db.additions
    additions.remove({'_id': ObjectId(addition_id)})
    return render_template("index.html", additions=mongo.db.additions.find())


@app.route('/edit_addition/<addition_id>')
def edit_addition(addition_id):
    addition = mongo.db.additions.find_one({'_id': ObjectId(addition_id)})
    categories = mongo.db.categories.find()
    chapters = mongo.db.chapters.find()
    return render_template("editaddition.html", additions=addition, categories=categories, chapters=chapters)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=False)
