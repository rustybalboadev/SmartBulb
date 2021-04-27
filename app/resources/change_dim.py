import json
from flask_restful import Resource, reqparse
from app.utils import STAPI

def change_color_parser():
    parser = reqparse.RequestParser()
    parser.add_argument("level")
    return parser

class ChangeDim(Resource):
    def post(self):
        parser = change_color_parser()
        args = parser.parse_args()

        STAPI().changeDim(int(args["level"]))