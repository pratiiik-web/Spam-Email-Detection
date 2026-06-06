import streamlit as st
import pandas as pd
import re, string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB

@st.cache_resource
def train_model():
    df = pd.read_csv('Data/spam.csv', encoding='latin-1')
    df = df[['v1', 'v2']]
    df.columns = ['label', 'message']

    def clean_text(text):
        text = text.lower()
        text = re.sub(r'\d+', '', text)
        text = text.translate(str.maketrans('', '', string.punctuation))
        return text.strip()

    df['clean_msg'] = df['message'].apply(clean_text)
    df['label_num'] = df['label'].map({'ham': 0, 'spam': 1})

    tfidf = TfidfVectorizer(max_features=3000, stop_words='english')
    X = tfidf.fit_transform(df['clean_msg'])
    y = df['label_num']

    model = MultinomialNB()
    model.fit(X, y)
    return model, tfidf

model, tfidf = train_model()

st.set_page_config(page_title="Spam Detector", page_icon="📧")
st.title("📧 Spam Email Detector")
st.markdown("Enter a message below to check if it's spam or legitimate.")

message = st.text_area("Message", height=150,
    placeholder="e.g. Congratulations! You've won a FREE prize. Call now to claim!")

if st.button("Check Message"):
    if message.strip() == "":
        st.warning("Please enter a message.")
    else:
        def clean_text(text):
            text = text.lower()
            text = re.sub(r'\d+', '', text)
            text = text.translate(str.maketrans('', '', string.punctuation))
            return text.strip()

        cleaned = clean_text(message)
        vector  = tfidf.transform([cleaned])
        pred    = model.predict(vector)[0]
        prob    = model.predict_proba(vector)[0]

        st.divider()
        if pred == 1:
            st.error(f"🚨 SPAM detected — {prob[1]:.0%} confidence")
        else:
            st.success(f"✅ Legitimate message — {prob[0]:.0%} confidence")

        st.markdown("**Spam probability:** " + f"{prob[1]:.1%}")
        st.progress(float(prob[1]))

st.divider()
st.markdown("**Test these examples:**")
col1, col2 = st.columns(2)
with col1:
    st.code("FREE entry! Win £1000 cash prize. Call NOW!")
with col2:
    st.code("Hey, are we still meeting for lunch tomorrow?")