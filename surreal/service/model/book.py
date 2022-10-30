import datetime as dt

class Book:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.published_at = dt.datetime.now()