#!/usr/bin/env python3


from secrets import TMDB_API_KEY
import requests
# import json

query = 'Enemy+of+the+State'
url = 'https://api.themoviedb.org/3/search/movie?api_key=' + \
    TMDB_API_KEY+'&query=' + query
req = requests.get(url)
answer = req.json()
print(answer)
