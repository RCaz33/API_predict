import pickle
import sklearn
import joblib

from sklearn.preprocessing import MultiLabelBinarizer, MaxAbsScaler
from sklearn.feature_extraction.text import CountVectorizer
from xgboost import XGBClassifier

with open('multilabel_tag_binerizer.pkl', 'rb') as file:
    tag_label = pickle.load(file)
    
scaler = joblib.load("MaxAbsScaler.pkl")
    
with open('Fitted_countvectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)
    
classifier = joblib.load("XGBClassifierPredictor.pkl")

# Now we use the loaded vectorizer for transforming new text data



def predict_tag(text):
    X_new = vectorizer.transform(text)
    X_new = scaler.transform(X_new)
    Tag_predict = classifier.predict(X_new)
    Tag_proba = classifier.predict_proba(X_new)
    
    prob_ = []
    for i, probability in enumerate(Tag_proba[0]):
        if probability > 0.5:
            prob_.append(probability)

    tags = multilabel.inverse_transform(y_pred)[0]
    
    return tags, prob_
