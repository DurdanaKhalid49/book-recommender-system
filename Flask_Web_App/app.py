from flask import Flask, render_template, request
import joblib
import numpy as np
import os
app = Flask(__name__)

# Load model and data
book_pivot = joblib.load('model/book_pivot.pkl')
model = joblib.load('model/book_knn_model.pkl')
book_list = list(book_pivot.index)

def recommend_books(book_name, n_recommendations=5):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id, :].values.reshape(1, -1), n_neighbors=n_recommendations + 1)

    recommended_books = []
    for i in range(1, len(suggestions[0])):
        recommended_books.append(book_pivot.index[suggestions[0][i]])
    return recommended_books

@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = []
    selected_book = None
    n_recommendations = 5

    if request.method == 'POST':
        selected_book = request.form['book_name']
        n_recommendations = int(request.form['n_recommendations'])
        recommendations = recommend_books(selected_book, n_recommendations)

    return render_template('index.html',
                           book_list=book_list,
                           selected_book=selected_book,
                           recommendations=recommendations,
                           n_recommendations=n_recommendations)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))  # use Railway port or default to 8080
    app.run(host="0.0.0.0", port=port) 
