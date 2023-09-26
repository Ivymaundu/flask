from flask import Flask,render_template

# trying to create an instance of an app
#'app' is a variable that holds that instance.
# It can be named as anything else
app = Flask(__name__)

@app.route("/") # / means that it is the first route that will be accessed 

#every route has a python function and needs to be unique
#you can name it anything
def index():
    return render_template("index.html") #the response given back to the user

#this command creates a web server and rruns the app

@app.route("/hello")
def hello():
    return "Welcome my app"

@app.route("/welcome")
def welcome():
    return "Have fun while interacting with my web page"

app.run()