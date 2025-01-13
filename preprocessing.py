import pandas as pd
import numpy as np 
from sklearn.preprocessing import MinMaxScaler

def load_data():
    """
    Load the datasets (Users, Books, and Ratings).
    """
    users = pd.read_csv(r"D:\Portfolio Projects\Book Recommender System\data\Users.csv", low_memory=False)
    books = pd.read_csv(r"D:\Portfolio Projects\Book Recommender System\data\Books.csv", low_memory=False)
    ratings = pd.read_csv(r"D:\Portfolio Projects\Book Recommender System\data\Ratings.csv", low_memory=False)
    return users, books, ratings

def clean_data(users, books, ratings):
    """
    Clean and preprocess the datasets.
    """

    # Drop rows with missing values
    users.dropna(inplace=True)
    books.dropna(inplace=True)
    ratings.dropna(inplace=True)

    # Remove duplicate ratings
    ratings.drop_duplicates(subset=["User-ID","ISBN"],inplace=True)

    # Filter out users with too few ratings (Optional)
    user_rating_counts = ratings['User -ID'].value_counts()
    ratings = ratings[ratings['User -ID'].isin(user_rating_counts[user_rating_counts >= 5].index)]

    # Filter out books with too few ratings (optional)
    book_rating_counts = ratings['ISBN'].value_counts()
    ratings = ratings[ratings['ISBN'].isin(book_rating_counts[book_rating_counts >= 5].index)]

    return users, books, ratings

def merge_data(users, books, ratings):
    """
    Merge the datasets based on the common columns.
    """

    # Merge users and ratings on User-ID
    data = pd.merge(users, ratings, on='User-ID')

    # Merge with books
    data = pd.merge(data, books, on='ISBN')

    return data

def normalize_ratings(data):
    """
    Normalize the ratings to a scale of 0 to 1
    """
    scaler = MinMaxScaler(feature_range=(0,1))
    data['Rating'] = scaler.fit_transform(data[['Rating']])
    return data

def preprocess():
    """
    Main preprocessing function
    """

    # Load data
    users, books, ratings = load_data()

    # Clean data
    users, books, ratings = clean_data(users,books,ratings)

    # Merge data
    data = merge_data(users,books,ratings)

    # Normalize ratings
    data = normalize_ratings(data)

    # Save preprocessed data
    data.to_csv('D:/Portfolio Projects/Book Recommender System/data/preprocessed_data.csv', index=False)

    print("preprocessing completed and data saved!")

if __name__ == "__main__":
    preprocess()


