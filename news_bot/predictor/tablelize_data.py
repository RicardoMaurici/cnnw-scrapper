import pandas as pd

risk_dict = {'Baixo':1, 'Medio':2, 'Alto':3}
category_dict = {'Positiva':1, 'Corrupcao':2, 'Politica':3, 'Processo-Juridico':4,
'Crime':5, 'Economia':6, 'Manifestacao':7, 'Eleicoes':8, 'Dano-Ambiental':9}

path = 'predictor/news.tsv'

# read file into pandas using a relative path
news = pd.read_csv(path, delimiter=' ', quotechar='|',
    names=['index', 'message', 'risk', 'category'])
#Map the risks and category to numbers
news['risk'] = news.risk.map(risk_dict)
news['category'] = news.category.map(category_dict)
# how to define X, y, z (from the news data) for use with COUNTVECTORIZER
X = news.message
y = news.risk
z = news.category
