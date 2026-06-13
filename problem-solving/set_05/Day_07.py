import pandas as pd
import streamlit as st
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer

@st.cache_resource
def load_model():
    df = pd.read_csv("youtube_comments.csv")

    model = Pipeline([
        ('tdidf', TfidfVectorizer()),
        ('clf', LogisticRegression())
    ], memory="pipeline_cache_dir") 

    model.fit(df['comment'], df['label'])

    return model

model = load_model()

st.title("Youtube comment classifier")
st.write("Classify your comment as Toxic or supportive: ")
user_input = st.text_area("Enter a youtube comment")

if user_input:
    prediction = model.predict([user_input])[0]

    if prediction == "toxic":
        st.error("This comment is likely **Toxic**")
    else:
        st.success("This comment is **Supportive**")

