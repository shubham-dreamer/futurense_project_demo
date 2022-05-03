import flask

#making a variable app and using Flask function
app= flask.Flask(__name__)

app.config["DEBUG"]=True
@app.route('/',methods=['GET'])
def home():
    return "<h1>Distant Reading Archive</h1><p> this is a paragraph<p>"
app.run()