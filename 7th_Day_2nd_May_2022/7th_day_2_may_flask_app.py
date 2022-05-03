import flask
from flask import request,jsonify
app=flask.Flask(__name__)

app.config["DEBUG"]=True

#create some test data for our catalog in the form of a list of dictionaries.
books=[
    {'id':0,
     'title':'A fairy tale',
     'author':'Shubham',
     'first_sentence':'I like coffee',
     'year_published':'1992'
    },
    {'id':1,
     'title':'A Marvel movie',
     'author':'dreamer',
     'first_sentence':'I like super powers',
     'year_published':'1999'
    },
    {'id':2,
     'title':'3 states',
     'author':'Chetan Bhagat',
     'first_sentence':'Love has no language and culture barriers',
     'year_published':'2000'
    }
]

@app.route('/',methods=['GET'])
def home():
    return "Welcome to my first API"

@app.route('/books/all',methods=['GET'])
def api_all():
    return jsonify(books)

app.run()
