from flask_restful import reqparse

parser = reqparse.RequestParser()
parser.add_argument('url', required=True)
parser.add_argument('hypertext', required=True)
parser.add_argument('about', required=True)
