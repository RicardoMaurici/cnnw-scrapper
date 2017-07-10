from sklearn.cross_validation import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from tablelize_data import X, y, risk_dict

""" Split the data, vectorize and train the model for risk """

#split the data for train and test
X_risk_train, X_risk_test, y_train, y_test = train_test_split(X, y, random_state=1)
# import and instantiate CountVectorizer (with the min frequency
# of appearance in docs of 2, and removing accents)
risk_vect = CountVectorizer(min_df=2, strip_accents='ascii')
# learn training data vocabulary, then use it to create a document-term matrix
X_risk_train_dtm = risk_vect.fit_transform(X_risk_train)
# transform testing data (using fitted vocabulary) into a document-term matrix
X_risk_test_dtm = risk_vect.transform(X_risk_test)
#instantiate a logistic regression model
risk_lr = LogisticRegression()
#train the model
risk_lr.fit(X_risk_train_dtm, y_train)

def predictRisk(string_arg):
    text_tdm = risk_vect.transform([string_arg])
    text_tdm.toarray()
    text_pred_class = risk_lr.predict(text_tdm)
    return [k for k,v in risk_dict.iteritems()
                if v == text_pred_class[0]].pop()
