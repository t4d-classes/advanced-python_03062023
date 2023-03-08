""" rate api """

from flask import Flask, Response

app = Flask(__name__)

# decorator
@app.route("/")
def home():
    """ home """
    return "<h1>Hello, World!</h1>"

if __name__ == "__main__":
  app.run()