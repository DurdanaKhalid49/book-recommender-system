# 📚 Book Recommender System

An intelligent and interactive Book Recommender System that suggests similar books based on user preferences. Built with **Streamlit** for a clean and stylish dashboard interface, and powered by **K-Nearest Neighbors (KNN)** and **collaborative filtering** techniques using real-world book ratings data.

![Book Recommender System Demo](https://your-demo-screenshot-url-if-any)

---

## 🚀 Features

- 📖 Recommends books based on user-selected titles using KNN algorithm
- 📊 Uses pivoted ratings matrix of books and users
- 🔍 Option to select the **number of recommendations**
- 🧠 Intelligent model trained on filtered and processed book ratings
- 🖥️ Elegant and modern **Streamlit dashboard** for real-time interaction

---

## 🗂️ Project Structure
```bash
Book Recommender System/
│
├── data/
│ ├── Books.csv
│ ├── Users.csv
│ └── Ratings.csv
│
├── model/
│ ├── model.pkl
│ └── book_pivot.pkl
│
├── Streamlit_Dashboard/
│ └── app.py
| ├── model/
|   └──model.pkl
|   └── book_pivot.pkl
|   └──requirements.txt
|   └──README.md
│
├── model/ ← Optional directory to hold backups
│
└── README.md
```
---

## ⚙️ How It Works

1. **Data Preprocessing**
   - Loads and cleans data from Books, Users, and Ratings CSVs
   - Removes inactive users and books with fewer than 50 ratings
   - Creates a pivot matrix (books × users)

2. **Model Training**
   - Trains a KNN model using the sparse book-user matrix
   - Saves both the matrix and model using `joblib`

3. **Streamlit App**
   - Loads saved model and matrix
   - Allows user to select a book and number of suggestions
   - Displays top N recommended books with stylish UI

---

## 🛠️ Installation

### 1. **Clone the repository**
```bash
git clone https://github.com/durdanakhalid/book-recommender-system.git
cd book-recommender-system
```
### Create and activate virtual environment

```bash
python -m venv venv
source venv/Scripts/activate  # Windows
#or
source venv/bin/activate      # macOS/Linux
```
### Install dependencies
```bash
pip install -r requirements.txt
```
### Run Streamlit app
```bash
cd Streamlit_Dashboard
streamlit run app.py
```
📦 Deployment Options
✅ Localhost (default)

☁️ Deploy to platforms like Streamlit Cloud, Railway, or HuggingFace Spaces

Upload large model files (if needed) to Hugging Face Hub and fetch during runtime

💡 Future Enhancements
Add book cover images using external APIs (e.g., Google Books API)

Display more metadata (authors, publication year, etc.)

Implement content-based hybrid recommendation

Add dark/light theme toggle to dashboard

🧠 Tech Stack
Python 🐍

Pandas, NumPy

Scikit-learn, KNN

Streamlit – for dashboard

Joblib – for model persistence

## Author
### Durdana Khalid
Data Scientist
🔗 LinkedIn
🌐 Portfolio Website

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.
