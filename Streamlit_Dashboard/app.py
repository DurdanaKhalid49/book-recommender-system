import streamlit as st
import joblib
import numpy as np
import os
# === Load model and pivot table ===
book_pivot = joblib.load("Streamlit_Dashboard/model/book_pivot.pkl")
model = joblib.load("Streamlit_Dashboard/model/book_knn_model.pkl")

# === Page Config ===
st.set_page_config(page_title="📚 Book Recommender", layout="centered")
if os.path.exists("style.css"):
    with open("style.css") as f:
        st.markdown("<style>" + f.read() + "</style>", unsafe_allow_html=True)
else:
    st.warning("⚠️ style.css not found. Default styling applied.")


# === Title ===
st.markdown("<h1 class='app-title'>📚 Book Recommender System</h1>", unsafe_allow_html=True)

# === Input Box ===
book_list = list(book_pivot.index)
selected_book = st.selectbox("Search for a book:", book_list)
num_recs = st.slider("How many books would you like to see?", min_value=1, max_value=15, value=6)

# === Recommendation Logic ===
def recommend_books(book_name, n_recommendations):
    book_id = np.where(book_pivot.index == book_name)[0][0]
    distances, suggestions = model.kneighbors(
        book_pivot.iloc[book_id, :].values.reshape(1, -1),
        n_neighbors=n_recommendations + 1  # +1 to exclude selected book
    )
    recommended_books = []
    for i in range(1, len(suggestions[0])):
        recommended_books.append(book_pivot.index[suggestions[0][i]])
    return recommended_books


# === Recommend Button ===
if st.button("🔍 Recommend"):
    st.markdown(f"<h3 class='recommend-header'>Books similar to <i>{selected_book}</i>:</h3>", unsafe_allow_html=True)
    recs = recommend_books(selected_book, num_recs)
    for idx, title in enumerate(recs, start=1):
        st.markdown(f"<div class='book-item'>{idx}. {title}</div>", unsafe_allow_html=True)
