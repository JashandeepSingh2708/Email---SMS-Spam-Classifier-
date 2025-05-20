import streamlit as st
import pickle
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

# Load model and vectorizer
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
model = pickle.load(open('model.pkl', 'rb'))

ps = PorterStemmer()

# Text preprocessing
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()
    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)

# --- Streamlit Page Config ---
st.set_page_config(page_title="Spam Classifier", layout="centered")

# --- Custom CSS with Background Color, Button Hover, and Text Color ---
st.markdown("""
    <style>
        body {
            background-color: #e6f2ff;
        }
        .stApp {
            background-color: #26213b;
        }
        .main {
            padding: 2rem;
            border-radius: 10px;
            box-shadow: 0px 0px 15px rgba(0,0,0,0.1);
        }
        h1 {
            text-align: center;
            color: #003366;
        }
        /* Text area text color */
        .stTextArea textarea {
            font-size: 16px !important;
            color: white !important;
            background-color: #1e1e2f !important;
            border-radius: 8px !important;
        }
        /* Button styling */
        .stButton>button {
            background-color: #003366;
            color: white;
            font-weight: bold;
            padding: 10px 24px;
            border-radius: 8px;
            transition: 0.3s ease;
        }
        /* Hover effect */
        .stButton>button:hover {
            background-color: #0059b3;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)

# --- Title ---
st.markdown("<h1>Email / SMS Spam Classifier 🚫📩</h1>", unsafe_allow_html=True)

# --- Input Box ---
input_sms = st.text_area("Enter the message below:", height=150)

# --- Predict Button ---
if st.button("Predict"):
    transformed_sms = transform_text(input_sms)
    vector_input = tfidf.transform([transformed_sms])
    result = model.predict(vector_input)[0]

    if result == 1:
        st.markdown(
            "<h2 style='color: red; text-align: center;'>🚨 Spam Message Detected!</h2>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            "<h2 style='color: green; text-align: center;'>✅ Not Spam - Safe Message</h2>",
            unsafe_allow_html=True
        )
