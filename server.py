from flask import Flask
import json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/help", methods=["GET"])
def get_help():
    return "Here is some help!"


@app.route("/help", methods=["POST"])
def post_help():
    return json.dumps({"text": "Posting some help!"})