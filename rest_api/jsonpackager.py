from flask import jsonify

API_DATA_KEYS = (
    'title',
    'news_date',
    'scrapped_date',
    'domain',
    'url',
    'categories',
    'key_words',
    'people',
    'companies',
    'news_text'
)

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
        output = format_dict(raw, API_DATA_KEYS)
    else:
        output = [format_dict(x, API_DATA_KEYS) for x in raw]
    return jsonify(output)

def format_dict(raw_dict, keys_list):
    """
    Takes the raw dict and return a f formated one given a list of keys

    Parameters
    ----------
    raw_dict : dict
    keys_list : list

    Returns
    -------
    dict
        formated dict
    """
    return {key: raw_dict[key] for key in keys_list}
