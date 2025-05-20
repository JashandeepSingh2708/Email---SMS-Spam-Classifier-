# Email-SMS Spam Classifier:
 A complete end-to-end Email/SMS Spam Classifier project using the UCI SMS Spam Collection Dataset. It includes data cleaning, EDA, preprocessing, TF-IDF feature extraction, and multiple ML models. Achieved 97.1% accuracy and 100% precision using Multinomial Naive Bayes, deployed with an interactive Streamlit web app.


# 🚫📩 Email/SMS Spam Detection App

This repository contains a full pipeline for detecting spam in emails and SMS messages using Machine Learning and Natural Language Processing (NLP). Built with Python and Streamlit, this intuitive web app helps users classify messages as spam or not in real-time.

## 📚 Dataset
- **Source:** [UCI SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset)
- Contains 5,572 labeled SMS messages as `spam` or `ham`.

---

## 🛠️ Key Features

### ✅ Data Cleaning & Preparation
- Removed unnecessary columns and duplicates
- Converted categorical labels (`ham/spam`) to binary form
- Handled imbalanced class distribution during evaluation

### 📊 Exploratory Data Analysis (EDA)
- Compared word/sentence counts between spam and ham messages
- Visualized frequent words using word clouds
- Found that spam messages tend to be longer and contain more promotional language

### 🔄 Text Preprocessing
- Lowercasing, tokenization, punctuation and stopword removal
- Stemming with Porter Stemmer
- Final cleaned text used for vectorization

### 🧠 Model Building & Evaluation
Multiple classification models were evaluated using **TF-IDF** features:
| Model                     | Accuracy | Precision |
|--------------------------|----------|-----------|
| Multinomial Naive Bayes  | 97.1%    | 100%      |
| Random Forest Classifier | 97.5%    | 98.3%     |
| SVM (Sigmoid Kernel)     | 97.5%    | 97.5%     |
| Logistic Regression      | 95.8%    | 97.0%     |

📌 **Final Model Selected:** Multinomial Naive Bayes  
📌 **Reason:** Simple, fast, high **precision (100%)**, and strong **accuracy (97.1%)** – ideal for reducing false positives in spam detection.

---

## 🌐 Streamlit Web App
An elegant and responsive interface built with Streamlit.

### Features:
- Paste your SMS or email message
- Get instant spam prediction with styled feedback
- Customized dark-themed UI with CSS enhancements

🖼️ Screenshot:
![image](https://github.com/user-attachments/assets/abae03b1-1c8d-4157-bbe9-e8073070f2f6)
![image](https://github.com/user-attachments/assets/f0bfff81-000a-4dcc-a853-277743e0a6be)

