# Books Dataset Analysis

## Project Overview

This project explores a dataset of books, containing details such as titles, authors, publication years, and publisher information. The main objective is to analyze the dataset and derive insights or prepare it for further use cases like recommendation systems.

## Dataset Description

- **Dataset Name**: Books.csv
- **Number of Records**: 271,360
- **Columns**:
  - `ISBN`: Unique identifier for books.
  - `Book-Title`: Title of the book.
  - `Book-Author`: Author of the book.
  - `Year-Of-Publication`: Year the book was published.
  - `Publisher`: Publishing house.
  - `Image-URL-S`, `Image-URL-M`, `Image-URL-L`: URLs for book cover images (small, medium, and large).

## Project Steps

1. **Data Loading and Exploration**:
   - Inspect the structure of the dataset.
   - Analyze the types and range of data.

2. **Data Preprocessing**:
   - Handle missing or inconsistent values.
   - Clean and format columns for analysis.

3. **Exploratory Data Analysis (EDA)**:
   - Visualize trends in publication years and author popularity.
   - Investigate patterns and outliers.

4. **Use Case (Optional)**:
   - Prepare the dataset for machine learning or a recommendation system.

## Repository Structure

Books_Analysis_Portfolio/
    README.md
    requirements.txt
    data/
        Books.csv
    notebooks/
        analysis.ipynb
    src/
        preprocessing.py
