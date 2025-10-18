Anime Recommendation System

This project uses **Scrapy** to crawl anime data from [MyAnimeList.net](https://myanimelist.net).  
Since real user rating data was not available, the **user dataset was generated** synthetically for testing and model training.

---

## Dataset Information
**1. animes.csv**
The dataset contains **2050 anime entries** with the following key features:
- **Title** – name of the anime  
- **Score** – average community rating  
- **Rank** – ranking on MyAnimeList  
- **Popularity, Members, Episodes**  
- **76 genre attributes** (one-hot encoded) such as *Action, Romance, Mecha, Slice of Life,* etc.  
- **Synopsis & Link** for reference  

**2.anime_genre_binary.csv**
A one-hot encoded version of animes.csv, where each of the 76 genres is represented as a binary column.
This version is optimized for machine learning models and feature engineering.

Genres include:
Action, Adventure, Comedy, Drama, Fantasy, Romance, Sci-Fi, Slice of Life, Supernatural, Mecha, Isekai, and many others.

**3.list_of_users.csv**
This dataset contains 250 synthetic user profiles, each representing their genre preference strength (on a scale from 0 to 10).
These scores can be interpreted as how much a user enjoys each genre.
Column	Description
user_id	Unique user identifier
#Genre Columns	Numeric preference score for each genre (0–10)

**4.training_data.csv**
A synthetic interaction dataset simulating how users rate anime titles.

Column	Description
user_id:	Reference to user in list_of_users.csv
anime_id:	Reference to anime in animes.csv
score:	Rating given by the user (0–10 scale)


---

## System Overview
The recommendation system is built upon **two 3-layer neural networks**:
1. **Anime feature extractor** – encodes anime metadata and genre vectors.  
2. **User preference predictor** – estimates how much a user would like an anime.

---

## Features
- **Recommend suitable anime for new users** based on their selected preferences.  
- **Find similar anime** to a given title using vector similarity.  
- **Neural-network-based recommendation model** that learns feature patterns.  
- **Preprocessed genre dataset** for efficient training.  
- **Notebook environment** for experiments and visualization.  

*(The current version works on Jupyter Notebook only. GUI will be added in future updates.)*

---

##  Tech Stack
- **Python** (NumPy, Pandas, PyTorch/TensorFlow)
- **Scrapy** (for web crawling)
- **Jupyter Notebook** (for development)
- **Matplotlib 
---

## Future Plans
- Add GUI using **Streamlit** or **Flask**  
- Integrate **collaborative filtering** for better personalization  
- Expand dataset with **real user reviews or ratings**  
- Deploy model as a REST API or web app  

---

How to Run
```bash
# 1. Clone this repository
git clone https://github.com/namgau/Anime-Content-based-Recommendation-System.git
cd anime-recommendation

# 2. Install dependencies
pip install -r requirements.txt

# 3. Open Jupyter Notebook
jupyter notebook

# 4. Run main notebook
Open "Anime_Recommendation_Notebook.ipynb" and execute all cells
