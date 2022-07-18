from doctest import master
from TweetRetrieval import get_input
from WatsonNLU import analyze
import os

if __name__ == '__main__':

    # Get relevant tweets
    df = get_input()

    master_text = ''

    # Iterate through rows of dataframe and build single text
    for row in df["text"]:
        master_text += row + ' '
    
    print(len(master_text))
    # Get sentiment analysis from Watson NLU
    response = analyze(master_text)

    print('Sentiments Analyzed!')

    print(response)

