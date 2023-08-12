# Importing the required libraries
from flask import Flask, jsonify
import datetime
from flask import request # used to parse payload
from flask import abort # used to send error status codes
from flask import render_template # used to render html pages
from urllib.parse import urlparse # used to parse youtube url
from urllib.error import URLError # used to catch invalid url errors



# define a variable to hold you app
app = Flask(__name__)

# define your resource endpoints
app.route('/')
def index_page():
    return  render_template('index.html')

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())

# server the app when this file is run
if __name__ == 'main':
    app.run(debug=True)

