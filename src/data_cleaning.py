#Importing the libraries
import pandas as pd
import numpy as np
import re
from nltk.corpus import stopwords

#Calling the data
data = pd.read_csv('./data/mpst_full_data.csv')
print(data.head())

#drop irrelevant columns
data.drop(columns=['split','synopsis_source'],inplace=True)

#Reduce the rows to 500
data = data.sample(500, random_state=42)

#Text cleaning
def clean_text(text):
    # Remove HTML tags
    text = re.sub(r'<.*?>', '', text)
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove extra spaces
    text = re.sub(r'\s+', ' ', text)
    # Convert to lowercase
    text = text.lower()
    # Remove stopwords
    text = ' '.join([word for word in text.split() if word not in stopwords.words('english')])
    # Remove leading and trailing spaces
    text = text.strip()
    # Remove multiple spaces
    text = re.sub(r'\s+', ' ', text)
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    return text
# Apply the clean_text function to the 'synopsis' column
data['plot_synopsis'] = data['plot_synopsis'].apply(clean_text)

# Remove duplicates
data.drop_duplicates(subset='plot_synopsis', inplace=True)

#Rename the columns
data.rename(columns={'plot_synopsis': 'synopsis', 'imdb_id': 'id'}, inplace=True)

# Save the cleaned data
data.to_csv('./data/data.csv', index=False)