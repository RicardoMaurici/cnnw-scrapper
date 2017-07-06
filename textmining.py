# coding=utf-8

from unicodedata import normalize

characters_to_remove = ('"','“','”','\\','`','*','_','{','}','[',']','(',')','>',
'#','+','-','.','!','$','\'',',','/',':','<','%')

def removeAccents(string_param, codif='utf-8'):
    '''
    Remove accents of a string
    '''
    return normalize('NFKD', string_param.decode(codif)).encode('ASCII','ignore')

def removeChars(string_param):
    '''
    Remove the characters (listed in characters_to_remove) of a string
    '''
    clean_string = string_param
    for char in characters_to_remove:
        clean_string = clean_string.replace(char, ' ')
    return clean_string

def clearString(string_param):
    return removeAccents(removeChars(string_param))
