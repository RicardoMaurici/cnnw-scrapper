from flask import Flask, Response
from flask import request
from flask import make_response as apiResponse
from jsonpackager import jsonRaw
from flask_pymongo import PyMongo


api = Flask(__name__)

api.config['MONGO_DBNAME'] = 'heroku_h5f5b7fv'
api.config['MONGO_URI'] = 'mongodb://heroku_h5f5b7fv:h6hgi06v9nc0asucuj93h5dn4a@ds127842.mlab.com:27842/heroku_h5f5b7fv'

mongo = PyMongo(api)

@api.route('/api', methods=['GET'])
def get_all_tests():
    document = mongo.db.test.find()
    return apiResponse(jsonRaw(document))


@api.route('/api/<name>', methods=['GET'])
def get_one_tests(name):
    document = mongo.db.test.find_one({'name':name})
    return apiResponse(jsonRaw(document))

@api.route('/api/<name>', methods=['POST'])
def post_one_tests(name):
    tests = mongo.db.test

    newDocummentName = name
    newDocummentNumber = request.json['number']
    newDocummentExtra_field = request.json['extra_field']

    newDocummentId = tests.insert({'name': newDocummentName,
                                   'number': newDocummentNumber,
                                   'extra_field':newDocummentExtra_field
                                   })

    output = None
    if tests.find_one({'_id': newDocummentId }):
        output = 'Error while inserting'
    else:
        output = 'Inserted'

    return jsonify({'result' : output})

if __name__ == '__main__':
    api.run(debug=True)
