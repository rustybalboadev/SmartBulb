import json
from flask_restful import Resource, reqparse
from app.utils import STAPI

def change_color_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("h")
    parser.add_argument("s")
    parser.add_argument("v")
    return parser

class ChangeColor(Resource):
    def post(self):
        parser = change_color_parser()
        args = parser.parse_args()

        STAPI().changeColor(STAPI.adjustHueBase(int(args["h"])), int(args["v"]), int(args["s"]))