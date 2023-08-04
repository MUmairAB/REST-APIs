"""
This is a simple Flask App.
"""

from flask import Flask

#Instantiate the app
app = Flask(__name__)


@app.route('/')
def hello():
    return "<h1>Hello World<h1>"

@app.route("/home", methods=["GET"])
def home_fun():
  return "<h1>Welcome to my Flask Website<h1>"

#Define the main function
if __name__ == "__main__":
    app.run()
