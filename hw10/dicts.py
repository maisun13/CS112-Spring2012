#!/usr/bin/env python
"""
dicts.py

Dictionaries
============================================================ 
In this section, write some functions which build and 
manipulate python dictionaries.
"""

# 1. freq
#      Return a dictionary of the number of times each value
#      is in data.
#          >>> freq([ 1, 2, 2, 2, 2, 3, 4, 5, 1, 4, 1, 9, 10 ])
#          { 1: 3, 2: 4, 3: 1, 4: 1, 5: 1, 9: 1, 10: 1}

def freq(data):
    "calculates the frequency for each value in data"

    freq = {}

    for value in data:

        if not value in freq:

            freq[value] = 0
        freq[value] += 1

    return freq

# 2. Movie Reviews
#      Write two functions to help with scoring a movie.
#
#      score:
#        stores a score in the "movies" dictionary
#
#      avg_score:
#        returns the average score of a movie
#
#      Examples:
#      >>> score("Fargo", 4)
#      >>> score("Fargo", 5)
#      >>> score("Fargo", 5)
#      >>> avg_score("Fargo")
#      4.6666666667
#      >>> avg_score("missing movie")
#      None

movies = {}

def score(title, value):
    "registers the score for a given movie out of 5"

    if not title in movies:
        movies[title] = []

    movies[title].append(value)

def avg_score(title):
    "returns the average score for a given movie"
    
    total = float(0)

    if not title in movies:
        return None

    ## Averages the score of the movie. ##
    for value in movies[title]:
        total += value

    return total / len (movies[title])


