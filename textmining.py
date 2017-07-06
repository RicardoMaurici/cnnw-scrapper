# coding=utf-8


from unicodedata import normalize

def removeAccents(txt, codif='utf-8'):
    return normalize('NFKD', txt.decode(codif)).encode('ASCII','ignore')

characters_to_remove = ('"','“','”','\\','`','*','_','{','}','[',']','(',')','>',
'#','+','-','.','!','$','\'',',','/',':','<','%')

def removeChars(string_param):
    '''
    Remove the characters (listed in characters_to_remove) of a string
    '''
    clean_string = string_param
    for char in characters_to_remove:
        clean_string = clean_string.replace(char, ' ')
    clean_string = removeAccents(clean_string)
    return clean_string
