from copyreg import constructor
import flask
from datetime import datetime
from TweetRetrieval import get_tweets
from WatsonNLU import analyze
from flask import request, jsonify

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    return flask.render_template('index.html')

@app.route('/hashtag', methods=['GET'])
def get_hashtag_emotions():
    
    print('GOT REQUEST')
    hashtag = '#' + request.args.get('hashtag')
    print('The hashtag is ' + str(hashtag))

    # Get todays date
    date_since = datetime.today().strftime('%Y-%m-%d')
    print('Date since: ' + date_since)
    
    df = get_tweets(hashtag, date_since)

    # Iterate through rows of dataframe and build single text
    master_text = ''
    for row in df["text"]:
        master_text += row + ' '
    
    # Get sentiment analysis from Watson NLU
    response = analyze(master_text)

    return jsonify(response)
