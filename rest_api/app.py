# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from flask import Flask, Response, jsonify, request
from flask import make_response as apiResponse
from utilApi import jsonRaw, format_dict, API_DATA_KEYS, API_DOC
from flask_pymongo import PyMongo

api = Flask(__name__)

api.config['MONGO_DBNAME'] = 'heroku_h5f5b7fv'
api.config['MONGO_URI'] = 'mongodb://heroku_h5f5b7fv:h6hgi06v9nc0asucuj93h5dn4a@ds127842.mlab.com:27842/heroku_h5f5b7fv'

mongo = PyMongo(api)

@api.route('/api/v1/news', methods=['GET', 'POST', 'OPTIONS'])
def api_news():
    """
    News Api for neoway-one team Project

    For more info:

    OPTIONS on /api/v1/news

    Parameters
    ----------
    None

    Returns
    -------
    json
        json of the filtered news

    """
    if request.method == 'GET':
        filters_keys = [key for key in request.args.keys() if key in API_DATA_KEYS]
        filter_dict = format_dict(request.args.to_dict(), filters_keys)
        all_documents = mongo.db.news.find(filter_dict)
        if all_documents.count() > 0:
            return apiResponse(jsonRaw(all_documents))
        else:
            return apiResponse('',404)

    elif request.method == 'POST':
        news_collection = mongo.db.news
        newDocummentId = news_collection.insert(format_dict(request.json, API_DATA_KEYS))
        if news_collection.find_one({'_id': newDocummentId }):
            return apiResponse(jsonify({'_id': str(newDocummentId) }), 201)
        else:
            return apiResponse('Could not create resource', 400)

    elif request.method == 'OPTIONS':
        return apiResponse(API_DOC)

    else:
        return apiResponse('',405)


if __name__ == '__main__':
    api.run(debug=True)
