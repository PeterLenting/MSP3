import os
from flask import Flask, render_template, redirect, request, url_for
from flask_pymongo import PyMongo # To connect Flask to the MongoDB
from bson.objectid import ObjectId # Convert in Bson-object to retrieve record in MongoDB by report ID
# settings.py
#from dotenv import load_dotenv
#load_dotenv()
# OR, explicitly providing path to '.env'
#from pathlib import Path
#env_path = Path('.') / '.env'
#load_dotenv(dotenv_path=env_path)


app = Flask(__name__)
app.config["MONGO_DBNAME"] = 'on_the_road'
app.config["MONGO_URI"] = 'mongodb+srv://OmeCor:OmeCor2@myfirstcluster-sykdi.mongodb.net/on_the_road?retryWrites=true&w=majority'
#app.config["MONGO_DBNAME"] = os.getenv("MONGO_DBNAME")
#app.config["MONGO_URI"] = os.getenv("MONGO_URI")

# Create an instance of PyMongo. Add the app into it with a constructor method.
mongo = PyMongo(app)

"""
- Make connection to the database
- render a template
"""
@app.route('/')
@app.route('/get_index')
def get_index():
    return render_template("index.html", additions=mongo.db.additions.find().sort('current_date', -1))


@app.route('/about')
def about():
    return render_template("about.html")


@app.route('/delete_addition/<addition_id>')
def delete_addition(addition_id):
    additions = mongo.db.additions
    # connecting with the correct addition in the database
    additions.remove({'_id': ObjectId(addition_id)})
    return redirect(url_for('get_index'))


@app.route('/add_addition')
def add_addition():
    categories = mongo.db.categories.find().sort('category_part', 1)
    chapters = mongo.db.chapters.find().sort('chapter', 1)
    return render_template('addaddition.html',  categories=categories, chapters=chapters)


@app.route('/insert_addition', methods=['POST'])
def insert_addition():
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
            'current_date': request.form.get('current_date'),
            'date': request.form.get('date'),
            'part_of_book': value2,
            'quote_in_book': request.form.get('quote_in_book'),
            'name_visitor': request.form.get('name_visitor'),
            'experience': request.form.get('experience'),
        }
    )
    return redirect("get_index")


@app.route('/edit_addition/<addition_id>')
def edit_addition(addition_id):
    # connecting with the correct addition in the database
    addition = mongo.db.additions.find_one({'_id': ObjectId(addition_id)})
    categories = mongo.db.categories.find()
    chapters = mongo.db.chapters.find()
    return render_template("editaddition.html", additions=addition, categories=categories, chapters=chapters)


@app.route('/update_addition/<addition_id>', methods=['POST'])
def update_addition(addition_id):
    addition = mongo.db.additions
    value = int(request.form.get('chapter_in_book'))
    value2 = int(request.form.get('part_of_book'))
    addition.update({'_id': ObjectId(addition_id)},
        {
            'city': request.form.get('city'),
            'chapter_in_book': value,
            'location': request.form.get('location'),
            'current_date': request.form.get('current_date'),
            'date': request.form.get('date'),
            'part_of_book': value2,
            'quote_in_book': request.form.get('quote_in_book'),
            'name_visitor': request.form.get('name_visitor'),
            'experience': request.form.get('experience'),
        }
    )
    return redirect(url_for('get_index'))


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)
