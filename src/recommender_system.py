import pandas as pd
import joblib
import numpy as np

# Load the saved book_pivot DataFrame and KNN model
book_pivot = joblib.load('D:/Portfolio Projects/Book Recommender System/src/book_pivot.pkl')
model = joblib.load('D:/Portfolio Projects/Book Recommender System/src/model.pkl')

def recommend_book(book_name):
    # Example check for a missing or invalid book name
    if not book_name:
        return ["Invalid book name provided!"]

    try:
        # Get the recommendations
        book_index = book_pivot.index.get_loc(book_name)  # Ensure book_name exists
        distances, indices = model.kneighbors(book_pivot.iloc[book_index, :].values.reshape(1, -1))

        recommendations = [book_pivot.index[idx] for idx in indices.flatten()]
        return recommendations[1:]  # Exclude the input book from recommendations
    except KeyError:
        return ["Book not found in the dataset!"]
