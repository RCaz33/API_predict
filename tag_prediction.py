import pickle
import sklearn
import joblib

from sklearn.preprocessing import MultiLabelBinarizer, MaxAbsScaler
from sklearn.feature_extraction.text import CountVectorizer
from xgboost import XGBClassifier

vectorizer = joblib.load("Fitted_countvectorizer.pkl")
scaler = joblib.load("MaxAbsScaler.pkl")
classifier = joblib.load("XGBClassifierPredictor.pkl")
tag_label = joblib.load("multilabel_tag_binerizer.pkl")

# Now we use the loaded vectorizer for transforming new text data

def predict_tag(text):
    X_new = vectorizer.transform([text])
    X_new = scaler.transform(X_new)
    Tag_proba = classifier.predict_proba(X_new)

    tags = tag_label.classes_
    top_values = sorted(enumerate(Tag_proba[0]), key=lambda x: x[1], reverse=True)[:3]
    
    tag_predict=[]
    tag_proba=[]
    for index, value in top_values:
        tag_predict.append(tags[index])
        tag_proba.append(round(value*100))
    
    return tag_predict, tag_proba
