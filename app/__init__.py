from flask import Flask, render_template
from flask_restful import Api, reqparse

app = Flask(__name__)
api = Api(app)

@app.route("/")
def root():
    return render_template("index.html")

from app.resources import ChangeColor, ChangeDim
api.add_resource(ChangeColor, "/changeColor")
api.add_resource(ChangeDim, "/changeDim")