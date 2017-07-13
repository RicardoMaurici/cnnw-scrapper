import requests
import json

API_URL = 'http://nw1-mongo-api.herokuapp.com/news'

def checkExistence(url):
    '''
    Checks if the news already exists in the mongodb
    returns True is exists and Flase if doesn't
    ---
    Input:
        filter url (string)
    ---
    Output:
        news existence (boolean)
    '''
    search_url = API_URL+'?url='+url
    r = requests.get(search_url)
    return (r.status_code == 200)

def storeNews(news):
    '''
    Stores the news in the mongodb via api
    Returns if the operation was successful
    ---
    Input:
        news (dict)
    ---
    Output:
        operation status (boolean)
    '''
    headers = {'content-type': 'application/json'}
    url = API_URL
    data = json.dumps(news)
    r = requests.post(url, data=data, headers=headers)
    return (r.status_code == 201)
