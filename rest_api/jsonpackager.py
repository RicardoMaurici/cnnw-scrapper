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
        output = format_dict(raw)
    else:
        output = [format_dict(x) for x in raw]
    return jsonify(output)

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
    return {key: raw_dict[key] for key in API_DATA_KEYS}
