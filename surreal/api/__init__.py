from flask import Blueprint
from flask_restful import Api
from .book import Book
from .process import Process, ProcessList

routes = Blueprint('api', __name__)

api = Api(routes)

api.add_resource(Book, '/books/<string:id>')
api.add_resource(Process, *['/processes', '/processes/<string:id>'])
api.add_resource(ProcessList, '/processes')