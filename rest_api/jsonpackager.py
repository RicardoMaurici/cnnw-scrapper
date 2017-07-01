from flask import jsonify

def jsonRaw(raw):

    output = []
    if type(raw) is dict:
        output = format_dict(raw)
    else:
        for q in raw:
            output.append(format_dict(q))
    return jsonify({'result': output})

def format_dict(raw_dict):
    return {'name':raw_dict['name'],
            'number': raw_dict['number'],
            'extra_field':raw_dict['extra_field']
            }
