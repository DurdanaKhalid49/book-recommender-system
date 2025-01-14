from flask import Flask, jsonify, render_template, request
import pandas as pd


from recommender_system import recommend_book

app = Flask(__name__,template_folder='D:/Portfolio Projects/Book Recommender System/src/templates')

# Home route to show the input form
@app.route("/")
def home():
    return render_template('index.html')

# Route to handle the book recommendation logic
@app.route("/recommend",methods=['POST'])
def recommend():
 # Get the book name from the user input
    book_name = request.form.get('book_name')
    
    if book_name is None:
        return "Error: book_name field is missing", 400
    # Call the recommendation function
    recommendations = recommend_book(book_name)
    # Pass recommendations to the template
    return render_template('recommendations.html', book_name=book_name, recommendations=recommendations)

    
if __name__ == "__main__":
    app.run(debug=True)
