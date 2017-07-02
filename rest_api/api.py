# encoding: utf-8
# encoding: iso-8859-1
# encoding: win-1252

from flask import Flask, Response, jsonify, request
from flask import make_response as apiResponse
from jsonpackager import jsonRaw, format_dict, API_DATA_KEYS
from flask_pymongo import PyMongo

api = Flask(__name__)

api.config['MONGO_DBNAME'] = 'heroku_h5f5b7fv'
api.config['MONGO_URI'] = 'mongodb://heroku_h5f5b7fv:h6hgi06v9nc0asucuj93h5dn4a@ds127842.mlab.com:27842/heroku_h5f5b7fv'

mongo = PyMongo(api)

@api.route('/api/v1/news', methods=['GET', 'POST', 'OPTIONS'])
def api_news():
    if request.method == 'GET':
        all_documents = mongo.db.news.find()
        return apiResponse(jsonRaw(all_documents))

    elif request.method == 'POST':
        news_collection = mongo.db.news
        newDocummentId = news_collection.insert(format_dict(request.json))
        print newDocummentId
        if news_collection.find_one({'_id': newDocummentId }):
            return apiResponse(jsonify({'_id': str(newDocummentId) }), 201)
        else:
            return apiResponse('', 400)

    elif request.method == 'OPTIONS':
        return "options"

    else:
        return apiResponse('',405)

if __name__ == '__main__':
    api.run(debug=True)
