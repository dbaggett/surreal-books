from flask_restful import Resource
from surreal.service.library import Library
from .model.book import BookSchema

# Book resource
class Book(Resource):
    def __init__(self):
        self.library = Library()
        self.book_schema = BookSchema()

    # Retrieve Book by ID
    def get(self, id):
        book = self.library.check_out(id)
        return self.book_schema.dump(book)
