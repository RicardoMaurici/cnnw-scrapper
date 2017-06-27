from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo


api = Flask(__name__)

api.config['MONGO_DBNAME'] = 'heroku_h5f5b7fv'
api.config['MONGO_URI'] = 'mongodb://heroku_h5f5b7fv:h6hgi06v9nc0asucuj93h5dn4a@ds127842.mlab.com:27842/heroku_h5f5b7fv'

mongo = PyMongo(api)

@api.route('/api', methods=['GET'])
def get_all_tests():
    tests = mongo.db.test

    output =[]
    for q in tests.find():
        output.append({'name':q['name'], 'number': q['number'], 'extra_field':q['extra_field']})

    return jsonify({'result': output})


@api.route('/api/<name>', methods=['GET'])
def get_one_tests(name):
    tests = mongo.db.test

    document = tests.find_one({'name':name})

    if document:
        output = {'name':document['name'], 'number': document['number'], 'extra_field':document['extra_field']}
    else:
        output = 'No results Found'

    return jsonify({'result': output})

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
