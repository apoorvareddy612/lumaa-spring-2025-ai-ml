import pandas as pd
import numpy as np
import sys
import nltk
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import spacy

# Download required NLTK datasets
nltk.download("stopwords")
nltk.download("punkt")
nltk.download("wordnet")

# Load dataset
data = pd.read_csv("./data/data.csv")

# Text Preprocessing
stop_words = set(stopwords.words("english"))
lemmatizer = WordNetLemmatizer()

def preprocess_text(text):
    tokens = word_tokenize(text)  # Tokenization
    tokens = [lemmatizer.lemmatize(word) for word in tokens if word.lower() not in stop_words]  # Lemmatization & stopwords removal
    return " ".join(tokens)

data["synopsis"] = data["synopsis"].apply(preprocess_text)

# TF-IDF Vectorization with fine-tuned parameters
vectorizer = TfidfVectorizer(
    max_df=0.85,  # Ignore overly common words
    min_df=2,  # Ignore rare words
    ngram_range=(1, 3),  # Use unigrams & bigrams
    stop_words="english"
)

tfidf_matrix = vectorizer.fit_transform(data["synopsis"] + ' ' + data['tags'])

# Query Expansion
def expand_query(query):
    # Load the SpaCy language model
    nlp = spacy.load("en_core_web_sm")

    # Process the query with SpaCy
    doc = nlp(query)

    # Keep only nouns, verbs, and adjectives
    tokens = [token.text for token in doc if token.pos_ in ['NOUN', 'VERB', 'ADJ']]

    expanded_terms = set(tokens)
    return " ".join(expanded_terms)

# Function to Recommend Movies
def recommend_movies(user_query, top_n=5):
    expanded_query = expand_query(user_query)
    print(f"Expanded Query: {expanded_query}")
    
    query_vector = vectorizer.transform([expanded_query])
    
    # Compute cosine similarity
    similarity_scores = cosine_similarity(query_vector, tfidf_matrix).flatten()
    
    # Normalize TF-IDF scores to [0,1]
    data['tfidf_score'] = (similarity_scores - np.min(similarity_scores)) / (np.max(similarity_scores) - np.min(similarity_scores) + 1e-6)

    # Return top N recommended movies
    recommendations = data.sort_values(by="tfidf_score", ascending=False).head(top_n)[["title", "tags", "tfidf_score"]]
    return recommendations

# Ensure a user input is provided
if len(sys.argv) < 2:
    print("Usage: python fine-tuned.py \"Your movie preference description\"")
    sys.exit(1)

# Get user input from command-line arguments
user_query = sys.argv[1]

# Get recommendations
recommendations = recommend_movies(user_query)

# Print recommendations
print("Recommended Movies:")
print(recommendations)

#Salary Expacted per month : $1600 - $2400