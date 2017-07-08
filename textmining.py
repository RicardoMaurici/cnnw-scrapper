# encoding: utf-8
import nltk
from unicodedata import normalize
from string import digits

characters_to_remove = (u'"',u'“',u'”',u'\\',u'`',u'*',u'_',u'{',u'}',u'[',u']',u'(',u')',u'>',
u'#',u'+',u'-',u'.',u'!',u'$',u'\'',u',',u'/',u':',u'<',u'%',u'º',u'ª',u'°')

def removeAccents(string_param, codif='utf-8'):
    '''
    Remove accents of a stringstring_param
    '''
    return normalize('NFKD', string_param.decode(codif)).encode('ASCII','ignore')

def removeChars(string_param, codif='utf-8'):
    '''
    Remove the characters (listed in characters_to_remove) of a string
    '''
    clean_string = string_param.decode(codif)
    for char in characters_to_remove:
        clean_string = clean_string.replace(char, ' ')
    return clean_string

def removeNumbers(string_param):
    '''
    Remove the numbers characters a string
    '''
    return string_param.translate(None, digits)

def stemmize(param):
    '''
    stemmize the word or a list of words
    '''
    stemmer = nltk.stem.RSLPStemmer()
    if type(param) == str:
        return stemmer.stem(param)
    elif type(param) == list:
        return [stemmer.stem(word) for word in param]
    else:
        raise ValueError('Type not suported')

def clearString(string_param):
    '''
    Return the string without special chars, digits and accents. Also stemm of the
    words
    '''
    cleanString = removeAccents(cleanString)
    cleanString = removeChars(string_param)
    cleanString = removeNumbers(cleanString)
    cleanString = stemmize(cleanString.split())
    cleanString = " ".join(cleanString)
    return cleanString
