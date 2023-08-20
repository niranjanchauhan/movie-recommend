



import pandas as pd
import numpy as np
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from surprise import Reader, Dataset, SVD, accuracy   
from surprise.model_selection import train_test_split


"""
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from ast import literal_eval
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from sklearn.metrics.pairwise import linear_kernel, cosine_similarity
from nltk.stem.snowball import SnowballStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import wordnet
from surprise import Reader, Dataset, SVD, evaluate
"""

import warnings; warnings.simplefilter('ignore')

# Source: https://www.kaggle.com/code/rounakbanik/movie-recommender-systems/notebook
# Simple Recommender:

# Load dataset
md = pd. read_csv('dataset/movies_metadata.csv')

# find mean
md['genres'] = md['genres'].fillna('[]').apply(literal_eval).apply(lambda x: [i['name'] for i in x] if isinstance(x, list) else [])
vote_averages = md[md['vote_average'].notnull()]['vote_average'].astype('int')
C = vote_averages.mean()

# Count Votes
vote_counts = md[md['vote_count'].notnull()]['vote_count'].astype('int')
m = vote_counts.quantile(0.95)
    
md['year'] = pd.to_datetime(md['release_date'], errors='coerce').apply(lambda x: str(x).split('-')[0] if x != np.nan else np.nan)

""" We use the TMDB Ratings to come up with our Top Movies Chart. 
We use IMDB's weighted rating formula to construct our chart. 
Mathematically, it is represented as follows:
    Weighted Rating (WR) =  ((v/v+m).R)+((m/v+m).C)
 
    where,
        v is the number of votes for the movie
        m is the minimum votes required to be listed in the chart
        R is the average rating of the movie
        C is the mean vote across the whole report

"""

def weighted_rating(x):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C)


# Top Movies List
def collect_movies(): 
    qualified = md[(md['vote_count'] >= m) & (md['vote_count'].notnull()) & (md['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity', 'genres']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    qualified['wr'] = qualified.apply(weighted_rating, axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    data = qualified.head(15)
    return data


s = md.apply(lambda x: pd.Series(x['genres']),axis=1).stack().reset_index(level=1, drop=True)
s.name = 'genre'
gen_md = md.drop('genres', axis=1).join(s)


def build_chart(genre, percentile=0.85):
    df = gen_md[gen_md['genre'] == genre]
    vote_counts = df[df['vote_count'].notnull()]['vote_count'].astype('int')
    vote_averages = df[df['vote_average'].notnull()]['vote_average'].astype('int')
    C = vote_averages.mean()
    m = vote_counts.quantile(percentile)
    
    qualified = df[(df['vote_count'] >= m) & (df['vote_count'].notnull()) & (df['vote_average'].notnull())][['title', 'year', 'vote_count', 'vote_average', 'popularity']]
    qualified['vote_count'] = qualified['vote_count'].astype('int')
    qualified['vote_average'] = qualified['vote_average'].astype('int')
    
    qualified['wr'] = qualified.apply(lambda x: (x['vote_count']/(x['vote_count']+m) * x['vote_average']) + (m/(m+x['vote_count']) * C), axis=1)
    qualified = qualified.sort_values('wr', ascending=False).head(250)
    
    return qualified


# Top Romantic movies
def romantic():
    data = build_chart('Romance').head(15)
    return data








# Content Based Recommender

links_small = pd.read_csv('dataset/links_small.csv')
links_small = links_small[links_small['tmdbId'].notnull()]['tmdbId'].astype('int')

md = md.drop([19730, 29503, 35587])
md['id'] = md['id'].astype('int')
smd = md[md['id'].isin(links_small)]

# Build a recommender using movie descriptions and taglines.
smd['tagline'] = smd['tagline'].fillna('')
smd['description'] = smd['overview'] + smd['tagline']
smd['description'] = smd['description'].fillna('')

tf = TfidfVectorizer(analyzer='word',ngram_range=(1, 2),min_df=0, stop_words='english')
tfidf_matrix = tf.fit_transform(smd['description'])

# Cosine Similarity
"""
We will be using the Cosine Similarity to calculate a numeric quantity that 
denotes the similarity between two movies. Mathematically, it is defined as follows:
    cosine(x,y) = x.y⊺/ ||x||.||y||

"""

cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

smd = smd.reset_index()
titles = smd['title']
indices = pd.Series(smd.index, index=smd['title'])

def get_recommendations(title):
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:31]
    movie_indices = [i[0] for i in sim_scores]
    return titles.iloc[movie_indices]


def similar1():
    data = get_recommendations('The Godfather').head(10)
    return data

def similar2():
    data = get_recommendations('The Dark Knight').head(10)
    return data







# Hybrid Recommender

def convert_int(x):
    try:
        return int(x)
    except:
        return np.nan
    

id_map = pd.read_csv('dataset/links_small.csv')[['movieId', 'tmdbId']]
id_map['tmdbId'] = id_map['tmdbId'].apply(convert_int)
id_map.columns = ['movieId', 'id']
id_map = id_map.merge(smd[['title', 'id']], on='id').set_index('title')
#id_map = id_map.set_index('tmdbId')

indices_map = id_map.set_index('id')

reader = Reader()
ratings = pd.read_csv('dataset/ratings_small.csv')
ratings.head()

data = Dataset.load_from_df(ratings[['userId', 'movieId', 'rating']], reader)
# data.split(n_folds=5)

svd = SVD()

trainset = data.build_full_trainset()
svd.fit(trainset)



def hybrid(userId, title):
    idx = indices[title]
    tmdbId = id_map.loc[title]['id']
    #print(idx)
    movie_id = id_map.loc[title]['movieId']
    
    sim_scores = list(enumerate(cosine_sim[int(idx)]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:26]
    movie_indices = [i[0] for i in sim_scores]
    
    movies = smd.iloc[movie_indices][['title', 'vote_count', 'vote_average', 'year', 'id']]
    movies['est'] = movies['id'].apply(lambda x: svd.predict(userId, indices_map.loc[x]['movieId']).est)
    movies = movies.sort_values('est', ascending=False)
    return movies.head(10)


def print1():
    data = hybrid(1, 'Avatar')
    return data

def print2():
    data = hybrid(500, 'Avatar')
    return data

def print3():
    data = hybrid(257, 'The Dark Knight')
    return data

def print4():
    data = hybrid(103, 'The Godfather')
    return data