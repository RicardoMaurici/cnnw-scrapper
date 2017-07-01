from flask import jsonify

def jsonRaw(raw):
    """
    Takes the raw input and return in the json format

    Parameters
    ----------
    raw : cursor object or dict

    Returns
    -------
    json
        json of the dicts

    """
    output = []
    if type(raw) is dict:
        output = format_dict(raw)
    else:
        for q in raw:
            output.append(format_dict(q))
    return jsonify({'result': output})

def format_dict(raw_dict):
    """
    Takes the raw dict and return a f formated one

    Parameters
    ----------
    raw_dict : dict

    Returns
    -------
    dict
        formated dict
    """
    return {'name':raw_dict['name'],
            'number': raw_dict['number'],
            'extra_field':raw_dict['extra_field']
            }
