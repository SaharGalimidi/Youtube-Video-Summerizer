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

@app.route('/')
def welcome_page():
    """
    This function renders the welcome page
    
    Returns:
        html: welcome page
    """
    return render_template('index.html')

@app.route('/api/summarize', methods=['GET'])
def get_video_id_from_url(url):
    """
    This function takes a YouTube URL and returns the video ID.

    Args:
        url: The YouTube URL.

    Returns:
        The video ID.
    """

    # Check if the URL is valid.
    try:
        components = urlparse(url)
    except URLError:
        # Invalid URL.
        print("Invalid URL:", url)
        return None

    # Check if the URL is a YouTube URL.
    if "youtube" not in components.hostname:
        # Not a YouTube URL.
        print("Not a YouTube URL:", url)
        return None

    # Get the video ID.
    path = components.path
    video_id = path.split("/")[-1]

    return jsonify(video_id)



# server the app when this file is run
if __name__ == '__main__':
    app.run()

