import pandas as pd
import re
import sys
from nltk.corpus import stopwords
import nltk

# Download stopwords if not already available
nltk.download("stopwords")

# Ensure a dataset file is provided
if len(sys.argv) < 2:
    print("Usage: python data_cleaning.py <dataset_filename>")
    sys.exit(1)

# Get dataset filename from command-line arguments
dataset_path = sys.argv[1]

# Load the dataset
data = pd.read_csv(f'./data/{dataset_path}')
print(data.head())

# Drop irrelevant columns
data.drop(columns=['split', 'synopsis_source'], inplace=True)

# Reduce the rows to 500
data = data.sample(500, random_state=42)

# Text cleaning function
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

# Apply the clean_text function to the 'plot_synopsis' column
data['plot_synopsis'] = data['plot_synopsis'].apply(clean_text)

# Remove duplicates
data.drop_duplicates(subset='plot_synopsis', inplace=True)

# Rename the columns
data.rename(columns={'plot_synopsis': 'synopsis', 'imdb_id': 'id'}, inplace=True)

# Save the cleaned data
output_path = "./data/data.csv"
data.to_csv(output_path, index=False)
print(f"Cleaned data saved to {output_path}")


#Salary Expacted per month : $1600 - $2400