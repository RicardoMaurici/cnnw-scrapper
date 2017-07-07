import nltk

#stem in portuguese example
stemmer = nltk.stem.RSLPStemmer()
print stemmer.stem('copiar')
print stemmer.stem('copiando')
print stemmer.stem('copiado')
print stemmer.stem('copia')

#simple test given a string return the unique stems of it
test_string = "Eu estava copiando o que estava copiado na copia que eu deveria "\
"ter copiado antes mesmo de copiar"
print test_string
list_of_words = test_string.split()
print list_of_words
list_of_words = [stemmer.stem(word) for word in list_of_words]
print list_of_words
print set(list_of_words)


#florest for tokeninzation
from nltk.corpus import floresta
#print floresta.tagged_sents()
