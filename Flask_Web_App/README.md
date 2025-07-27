# 📚 Book Recommender System – Flask Web App

Welcome to the **Book Recommender System**, a sleek and stylish web app built using **Flask** that helps users discover their next favorite read based on book similarity!

## 🔥 Features

- 📖 Recommends similar books based on user-selected input.
- 🔍 Lets users choose how many book recommendations they want.
- 🎨 Eye-catching, modern UI with smooth layout.
- ⚙️ Built using **Flask**, **Scikit-learn**, **Joblib**, and **HTML/CSS**.

---

## 🛠️ Tech Stack

| Tool           | Purpose                         |
|----------------|----------------------------------|
| Flask          | Web framework                   |
| Scikit-learn   | KNN Model (book similarity)     |
| Joblib         | Model & Data serialization      |
| HTML/CSS       | Frontend UI                     |
| Jupyter Notebook | Data preprocessing & modeling |

---

## 🚀 How It Works

1. The user selects a book title from a dropdown list.
2. They can also choose the number of recommendations they want.
3. The app uses **K-Nearest Neighbors (KNN)** to find similar books.
4. Recommended titles are displayed in a clean and elegant format.

---

## 📂 Project Structure
```bash
Book_Recommender_System_Web_App/
│
├── model/
│ ├── book_pivot.pkl # Pivot table of books vs users
│ └── model.pkl # Trained KNN model
│
├── static/
│ └── style.css # Custom CSS styles
│
├── templates/
│ └── index.html # HTML frontend
│
├── app.py # Main Flask app
├── requirements.txt # Dependencies
└── README.md # Project documentation
```

---

## 🧠 Model Details

- **Model**: `K-Nearest Neighbors (KNN)`
- **Data**: Merged `Books.csv`, `Users.csv`, `Ratings.csv` from Book-Crossing dataset.
- **Filtering**: Only users with >200 ratings and books with >50 ratings included.
- **Recommendation Basis**: User-item matrix pivoted on book titles.

---

## 🧪 Setup Instructions

### **Clone the repository**:

```bash
git clone https://github.com/yourusername/Book_Recommender_System_Web_App.git
cd Book_Recommender_System_Web_App
```
### Create virtual environment:

```bash
python -m venv venv
source venv/Scripts/activate  # On Windows
```
### Install dependencies:

```bash
pip install -r requirements.txt
```
### Run the Flask app:

```bash
python app.py
Visit in Browser:
Go to http://127.0.0.1:5000/
```
## Example Use
Choose "Animal Farm" from the dropdown.

Select 10 recommendations.

Get a list of 10 similar books instantly!


## Deployment
You can deploy this app using:

Railway

Render

Hugging Face Spaces (with Gradio or Flask)

Need help? I can walk you through it.

🙌 Acknowledgements
📚 Book data from Book-Crossing Dataset

💡 Inspired by collaborative filtering recommender systems

## Author
### Durdana Khalid
Data Scientist | Machine Learning Enthusiast
🔗 Portfolio | 💼 LinkedIn | 💻 GitHub

📬 Feedback & Contributions
If you have ideas, suggestions, or improvements, feel free to open an issue or submit a pull request. Let's grow this together!
