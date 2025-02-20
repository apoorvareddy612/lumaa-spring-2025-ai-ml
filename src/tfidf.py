#Importing libraries
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

#Recommendation function
'''This function takes user input and dataset as arguments and returns a list of recommended movies
It uses TF-IDF Vectorizer to convert text data into numerical data and cosine similarity to find similar movies
It returns a dataframe with the top 5 recommended movies
It uses the title, synopsis, and tags of the movies to find similar movies
It uses the cosine similarity to find similar movies'''

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
    data["tfidf_score"] = cosine_similarities

    # Sort by similarity score
    recommended_movies = data.sort_values(by="tfidf_score", ascending=False).head(5)

    # Display top recommendations
    return recommended_movies[["title", "tfidf_score"]]


data = pd.read_csv('./data/data.csv')
user_query = "I love thrilling action movies set in space, with a comedic twist."
recommendations = recommend_movies(user_query, data)
print(recommendations)