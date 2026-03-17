import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def load_data():
    return pd.read_csv("data/ratings.csv")

def create_matrix(data):
    return data.pivot_table(index='userId', columns='movieId', values='rating').fillna(0)

def compute_similarity(matrix):
    return cosine_similarity(matrix)

def build_model():
    data = load_data()
    matrix = create_matrix(data)
    similarity = compute_similarity(matrix)
    return matrix, similarity