from flask import Flask
from surreal.api import routes

# create Flask application
app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
def root():
    return 'Wrong Place.'