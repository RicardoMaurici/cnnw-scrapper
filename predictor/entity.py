import spacy
#import function of english translation

#instalation of the required package
os.system("python -m spacy download en")

#globals
encoding = 'utf-8'
nlp = spacy.load('en')

def predictPeople(string_arg):
    """
    Predicts the people of a news based on the news body
    ---
    Args: news body
        String
    ---
    Return: the entities
        List of strings
    """
    #add the translation function
    #string_arg = translate(string_arg)
    doc = nlp(unicode(string_arg, encoding))
    output =  [ent.text for ent in doc.ents if ent.label_ == 'PERSON']
    return list(set(output))

def predictCompanies(string_arg):
    """
    Predicts the companies of a news based on the news body
    ---
    Args: news body
        String
    ---
    Return: the entities
        List of strings
    """
    #add the translation function
    #string_arg = translate(string_arg)
    doc = nlp(unicode(string_arg, encoding))
    output =  [ent.text for ent in doc.ents if ent.label_ == 'ORG']
    output = list(set(output))
    #output = [translate(company) for company in output]
    return output
