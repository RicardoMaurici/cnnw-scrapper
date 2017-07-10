from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from tablelize_data import X, z, category_dict

""" Same as risk for category """

#split the data for train and test
X_ctg_train, X_ctg_test, z_train, z_test = train_test_split(X, z, random_state=1)
# import and instantiate CountVectorizer (with the min frequency
# of appearance in docs of 2, and removing accents)
ctg_vect = CountVectorizer(min_df=2, strip_accents='ascii')
# learn training data vocabulary, then use it to create a document-term matrix
X_ctg_train_dtm = ctg_vect.fit_transform(X_ctg_train)
# transform testing data (using fitted vocabulary) into a document-term matrix
X_ctg_test_dtm = ctg_vect.transform(X_ctg_test)
#instantiate a logistic regression model
ctg_lr = LogisticRegression()
#train the model
ctg_lr.fit(X_ctg_train_dtm, z_train)

def predictCategory(string_arg):
    text_tdm = ctg_vect.transform([string_arg])
    text_tdm.toarray()
    text_pred_class = ctg_lr.predict(text_tdm)
    return [k for k,v in category_dict.iteritems()
                if v == text_pred_class[0]].pop()
