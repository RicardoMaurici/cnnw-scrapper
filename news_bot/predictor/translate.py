from googletrans import Translator

PT_BR = 'pt'
ENG = 'en'

def translate(string, language):
    '''
    Translate a string of a lenguage to another lenguage
    ---
    Inputs:
        Text to be translated (string)
        Target lenguage (string)
    ---
    Output:
        Text translated to target lenguage (string)
    '''
    translator = Translator()
    translated =  translator.translate(string, dest=language)
    return translated.text
