from flask import Flask
from surreal.api import routes
from ma import mapper

# create Flask application
app = Flask(__name__)

app.register_blueprint(routes)

@app.route('/')
def root():
    return 'Wrong Place.'

if __name__ == '__main__':
    mapper.init_app(app)
    app.run(port=5000, debug=True, host='0.0.0.0')