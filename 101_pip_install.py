#jeden způsob
#import flask              ->
#app = flask.Flask(__name__)

#druhý způsob
#import flask as fl
#app = fl.Flask(__name__)

#třetí způsob
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1>AHOJ!!!</h1>"

if __name__ == "__main__":
    # Run the Flask development server
    app.run(host="0.0.0.0", port=5000, debug=True)