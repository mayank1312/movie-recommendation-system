# 🎬 Movie Recommender System

A content-based movie recommender system built with Python and Streamlit that suggests movies based on content similarity.

**[➡️ https://movie-recommendation-system-38nx.onrender.com/]**  ---

## 📖 About The Project

This project is a content-based movie recommender system. The model recommends 5 movies that are most similar to a movie selected by the user from a dataset of 5,000 movies from The Movie Database (TMDB).

The core of this project is the vectorization of movie details, where text data is converted into numerical vectors to calculate similarity scores between them.

---

## 🛠️ Built With

* **Frontend:** [Streamlit](https://streamlit.io/)
* **Backend/ML:** [Python](https://www.python.org/)
* **Libraries:** [Pandas](https://pandas.pydata.org/), [Scikit-learn](https://scikit-learn.org/)
* **Data Source:** [TMDB 5000 Movie Dataset on Kaggle](https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata)

---

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Data Manipulation:** Pandas,Numpy
- **Machine Learning:** Scikit-learn
- **Web Framework:** Streamlit
- **API:** The Movie Database (TMDB) API for fetching posters
- **Deployment:** Streamlit Community Cloud

---

## ⚙️ How It Works

The recommendation model follows these key steps:

1.  **Data Loading & Preprocessing:** The dataset is loaded, and key features like `genres`, `keywords`, `cast`, and `director` are extracted. These features are merged into a single `tags` column for each movie to create a content profile.

2.  **Feature Extraction (Vectorization):** The text data in the `tags` column is converted into numerical vectors using the **Bag of Words** technique via Scikit-learn's `CountVectorizer`. Each movie is represented as a vector in a high-dimensional space.

3.  **Similarity Calculation:** **Cosine Similarity** is used to calculate the similarity between every movie vector. This results in a similarity matrix where each movie has a score indicating its similarity to every other movie in the dataset.

4.  **Recommendation:** When a user selects a movie, the system looks up its similarity scores with all other movies, sorts them in descending order, and returns the top 5 most similar movies.

---

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

* Python 3.8 or higher
* Git LFS (for handling the large `.pkl` files)

### Installation

1.  **Clone the repository:**
    ```sh
    git clone [https://github.com/mayank1312/movie-recommendation-system.git]
    ```
2.  **Navigate to the project directory:**
    ```sh
    cd movies-recommender-system
    ```
3.  **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```
4.  **Run the Streamlit app:**
    ```sh
    streamlit run app.py
    ```
