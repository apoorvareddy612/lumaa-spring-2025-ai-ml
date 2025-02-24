# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation
---
## Setup
### Clone this Repository
 ```bash
 git clone https://github.com/apoorvareddy612/lumaa-spring-2025-ai-ml.git
 ```
### Change the path to this repo
 ```bash
 cd lumaa-spring-2025-ai-ml
 ```
### Python Version:
- This project requires Python 3.X

  Ensure you have Python installed by running:
  ```bash
  python --version
  ```
### Virtual Environment:
To set up a virtual environment in the cloned repository

**Create a virtual environment**:
  ```bash
  python3 -m venv venv
  ```
Activate the virtual environment:
- On Windows:
  ```bash
  venv\Scripts\activate
  ```
- On macOS/Linux:
  ```bash
  source venv/bin/activate
  ```
### Install Dependencies:
Once the virtual environment is activated. Inside the directory, install the project dependencies by running:
 ```bash
 pip install -r requirements.txt
 ```
---
## Dataset

- **Source**: The dataset used for the recommendation system comes from [Kaggle](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags/data?select=mpst_full_data.csv). It contains a collection of titles, plot synopsis and tags
- **Steps to Load**:
  - Download the dataset from [this link](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags/data?select=mpst_full_data.csv).
  - Place the dataset file (`mpst_full_data.csv`) in the `/data` directory.
  - Unzip the dataset 
  - The dataset includes columns such as `imdb_id`, `title`, `plot_synopsis`, and `tags`.
  - If necessary, preprocess the dataset by cleaning missing values or removing duplicates.

---
### Running code  
In this repository follow below : 
- **two folders**
  - data
  - src 
- **data**
  - data.csv, which is already cleaned and pre-processed 
- **src**
  - *data_cleaning.py*
  - *tfidf.py*
  - *fine-tuned.py* 
 
If you want to clean and pre-process on the original data, I recommend to download the data from [kaggle](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags/data?select=mpst_full_data.csv) and then run the **data_cleaning.py** 
  ```bash
  python ./src/data_cleaning.py mpst_full_data.csv
  ```
I have implemented two ways, one which is the base code and the other one is fine tuned on the top of it. \
**tfidf.py** is a base code file 
  ```bash
  python ./src/tfidf.py "I like action movies set in space"
  ```
**fine-tuned.py** is the fine tuned code
  ```bash
  python ./src/fine-tuned.py "I like action movies set in space"
  ```
### Results
The below image shows the compared results of tfidf and fine-tuned version of it \
![Screenshot 2025-02-23 at 4 39 29 PM](https://github.com/user-attachments/assets/89413de6-f99d-47d3-a26f-c6c78acda4d5)
