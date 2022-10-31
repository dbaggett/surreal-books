from flask_restful import abort, original_flask_make_response
from flask import jsonify
import json

class Error():
    def __init__(self, title, status, detail, instance, type = 'undefined'):
        self.title = title
        self.status = status
        self.detail = detail
        self.instance = instance
        self.type = type

def book_not_found_error(resource_id: str):
    abort(
        original_flask_make_response(
            jsonify(
                Error(
                    title = 'Not Found',
                    status = 404,
                    detail = f'Book with ID {resource_id} does not exist',
                    instance= f'/books/{resource_id}'
                ).__dict__
            ),
            404
        )
    )
