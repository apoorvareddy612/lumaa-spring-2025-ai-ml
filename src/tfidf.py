import pandas as pd
import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Recommendation function
def recommend_movies(user_input, dataset, top_n=5):
    # Combine title, synopsis, and tags for textual comparison
    dataset['combined_text'] = dataset['title'] + ' ' + dataset['synopsis'] + ' ' + dataset['tags']
    
    # Initialize TF-IDF Vectorizer
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(dataset['combined_text'])
    
    # Transform user input into vector
    user_tfidf = vectorizer.transform([user_input])
    
    # Compute cosine similarity
    cosine_similarities = cosine_similarity(user_tfidf, tfidf_matrix).flatten()
    
    # Add similarity scores to the dataframe
    dataset["tfidf_score"] = cosine_similarities

    # Sort by similarity score
    recommended_movies = dataset.sort_values(by="tfidf_score", ascending=False).head(top_n)

    # Display top recommendations
    return recommended_movies[["title","tags", "tfidf_score"]]

# Ensure a user input is provided
if len(sys.argv) < 2:
    print("Usage: python tfidf.py \"Your movie preference description\"")
    sys.exit(1)

# Get user input from command-line arguments
user_query = sys.argv[1]

# Load dataset
data = pd.read_csv('./data/data.csv')

# Get recommendations
recommendations = recommend_movies(user_query, data)

# Print recommendations
print(recommendations)


#Salary Expacted per month : $1600 - $2400