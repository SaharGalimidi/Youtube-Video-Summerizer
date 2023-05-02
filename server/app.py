# Initialize app.py file with basic Flask RESTful BoilerPlate with the tutorial link as mentioned in the Reference Section below.
# https://atmamani.github.io/blog/building-restful-apis-with-flask-in-python/
# for a YouTube video summarizer product. 
# The product will be developed as a Chrome extension using Flask and the summarizing will use NLP libraries, such as NLTK and spaCy, to extract the main ideas and key points from the transcript. 
# The transcript will be retrieved using youtube-transcript-api module.


# Importing the required libraries
import os
import sys
from flask import Flask, jsonify
import datetime
from flask import request # used to parse payload
from flask import abort # used to send error status codes
from flask import render_template # used to render html pages


# define a variable to hold you app
app = Flask(__name__)


# define your resource endpoints
app.route('/')
def index_page():
    return "Hello world"

app.route('/time', methods=['GET'])
def get_time():
    return str(datetime.datetime.now())

app.route('/hello')
def welcome_message():
    """
    Called as /hello?name='value'
    """
    # if user sends payload to variable name, get it. Else empty string
    name = request.get('name', '') 
    return f'Welcome {name}'

@app.route('/welcome')
def welcome_page():
    return render_template('index.html',
                            os_type=sys.platform,
                            os_name=os.name)



# server the app when this file is run
if __name__ == '__main__':
    app.run()

