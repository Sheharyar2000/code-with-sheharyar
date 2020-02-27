# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 13:45:00 2020

@author: home
"""

import nltk
nltk.download('vader_lexicon')
nltk.download('punkt')

# first, we import the relevant modules from the NLTK library
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# next, we initialize VADER so we can use it within our Python script
sid = SentimentIntensityAnalyzer()

# the variable 'message_text' now contains the text we will analyze.
message_text = '''i hate you.'''
message_text1 = '''i like you.'''
message_text2 = '''i know him.'''

print(message_text)
print(message_text1)
print(message_text2)

# Calling the polarity_scores method on sid and passing in the message_text outputs a dictionary with negative, neutral, positive, and compound scores for the input text
scores = sid.polarity_scores(message_text)
scores1 = sid.polarity_scores(message_text1)
scores2 = sid.polarity_scores(message_text2)

# Here we loop through the keys contained in scores (pos, neu, neg, and compound scores) and print the key-value pairs on the screen

for key in sorted(scores):
        print('{0}: {1}, '.format(key, scores[key]), end='')