# AI/Machine Learning Intern Challenge: Simple Content-Based Recommendation
---
## Dataset

- **Source**: The dataset used for the recommendation system comes from [Kaggle](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags/data). It contains a collection of titles, plot synopsis and tags
- **Steps to Load**:
  - Download the dataset from [this link](https://www.kaggle.com/datasets/cryptexcode/mpst-movie-plot-synopses-with-tags/data).
  - Unzip the dataset into a directory.
  - Place the dataset file (`mpst_full_data.csv`) in the `/data` directory.
  - The dataset includes columns such as `imdb_id`, `title`, `plot_synopsis`, and `tags`.
  - If necessary, preprocess the dataset by cleaning missing values or removing duplicates.

---

## Setup
### Clone this Repository
 ```bash
 git clone https://github.com/apoorvareddy612/lumaa-spring-2025-ai-ml.git
 ```
### Python Version:
- This project requires Python 3.10

  Ensure you have Python installed by running:
  ```bash
  python --version
  ```
### Virtual Environment:
To set up a virtual environment in the cloned repository

**Create a virtual environment**:
  ```bash
  python3.10 -m venv venv
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
Once the virtual environment is activated, install the project dependencies by running:
 ```bash
 pip install -r requirements.txt
 ```
### Running code  
In this repository follow below : \
two folders : data and src \
data consist of data.csv, which is already cleaned and pre-processed \
src consist of data_cleaning.py, tfidf.py and fine-tuned.py \
If you want to clean and pre-process on the original data, I recommend to download the data from kaggle and then run the data_cleaning.py 
  ```bash
  python ./src/data_cleaning.py mpst_full_data.csv
  ```
I have implemented two ways, one which is the base code and the other one is fine tuned on the top of it. \
tfidf.py is a base code file 
  ```bash
  python ./src/tfidf.py "I like action movies set in space"
  ```
fine-tuned.py is the fine tuned code
  ```bash
  python ./src/fine-tuned.py "I like action movies set in space"
  ```

5. **Summary & Instructions**  
   - A short `README.md` that includes:
     - **Dataset**: Where it’s from, any steps to load it.  
     - **Setup**: Python version, virtual environment instructions, and how to install dependencies (`pip install -r requirements.txt`).  
     - **Running**: How to run your code (e.g., `python recommend.py "Some user description"` or open your notebook in Jupyter).  
     - **Results**: A brief example of your system’s output for a sample query.

---

## Deliverables

3. **Short Video Demo**  
   - In a `.md` file (e.g., `demo.md`) within your fork, paste a link to a **brief screen recording** (video link).  
   - Demonstrate:
     - How you run the recommendation code.  
     - A sample query and the results.

4. **Deadline**  
   - Submit your fork by **Sunday, Feb 23th 11:59 pm PST**.

> **Note**: This should be doable within ~3 hours. Keep it **straightforward**—you do **not** need advanced neural networks or complex pipelines. A simple TF-IDF + cosine similarity approach is sufficient.

---

## Evaluation Criteria

1. **Functionality**  
   - Does your code run without errors?  
   - When given an input query, does it successfully output relevant items?

2. **Code Quality**  
   - Clear, commented code (where it counts).  
   - Logical steps (load data → transform → recommend).

3. **Clarity**  
   - Is your `README.md` straightforward about setup, how to run, and what to expect?

4. **ML/Recommendation Understanding**  
   - Basic implementation of a content-based recommendation approach (vectorization, similarity measure).

**We look forward to seeing your solution!** Good luck!
