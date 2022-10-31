from surreal.service.model.book import Book

# Library service which manages inventory of Books
class Library(object):
    def __init__(self):
        self.books = {
            "test": Book(id='test', title='Test Book', content='WIP')
        }
    
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Library, cls).__new__(cls)
        return cls.instance
    
    # Insert Book into "database"
    def check_in(self, book: Book):
        self.books[book.id] = book
    
    # Index a Book by ID from the "database"
    def check_out(self, book_id: str) -> Book or None:
        return self.books.get(book_id)