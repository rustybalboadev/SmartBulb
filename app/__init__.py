from flask import Flask, render_template
from flask_restful import Api, reqparse
from flask_socketio import SocketIO

app = Flask(__name__)
api = Api(app)

socket = SocketIO(app)

@app.route("/")
def root():
    from app.utils import STAPI
    h, s, v = STAPI().grabCurrent()

    return render_template("index.html", h=h, s=s, v=v)

from app.resources import ChangeColor, ChangeDim
api.add_resource(ChangeColor, "/changeColor")
api.add_resource(ChangeDim, "/changeDim")

from app.sockets.socket import new_color, new_dim