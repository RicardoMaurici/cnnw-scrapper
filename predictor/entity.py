import spacy
import os
from translate import translate, PT_BR, ENG

#instalation of the required package
#print "Installing 'en' package."
os.system("python -m spacy download en")

#globals
encoding = 'utf-8'
nlp = spacy.load('en')

def predictEntities(string_arg):
    """
    Predicts the entities of a news based on the news body
    ---
    Args: news body
        String
    ---
    Return: the entities
        List of strings
    """
    #translate to english
    string_arg = translate(string_arg, ENG)
    #feed the model
    doc = nlp(string_arg)
    #filter entities
    output =  [ent.text for ent in doc.ents if (ent.label_ == 'ORG' or
                    ent.label_ == 'PERSON')]
    #remove repeated
    output = list(set(output))
    #translate back to portuguese
    output = [translate(entity, PT_BR) for entity in output]
    return output
