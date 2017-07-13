# coding=utf-8
import re
import requests

API_URL = 'https://cnnw.herokuapp.com/api/v1/tags/'

def predictTags(string_param):
    '''
    Get the tags in the string based on the registereds in the API_URL
    ---
    Input:
        Text (string)
    ---
    Output:
        Matched tags (list of strings)
    '''
    #get the tags from the api
    r = requests.get(API_URL)
    tags = [tag_dict['name'] for tag_dict in r.json()]
    #search for the tags in the news body
    news_tags = [tag for tag in tags
        if re.search(re.compile(tag, re.IGNORECASE), string_param)]
    return news_tags
