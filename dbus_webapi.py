from flask import Flask
import api

app = Flask(__name__)
app.register_blueprint(api.blueprint, url_prefix='/api')

@app.route('/')
def hello_world():
    return 'Hello, World!\n API is working'
