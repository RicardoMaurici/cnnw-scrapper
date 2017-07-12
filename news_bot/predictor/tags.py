# coding=utf-8

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
    tags = [tag.lower() for tag in tags]
    #search for the tags in the news body
    splited_string = string_param.split()
    lowered_words = [word.lower() for word in splited_string]
    news_tags = [tag for tag in tags if tag in lowered_words]
    #return the finded ones
    return news_tags
