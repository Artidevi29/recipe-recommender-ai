from flask import Flask, render_template, request
import pandas as pd
import numpy as np
import os
import re
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# ------------------- DATA LOADING (with fallback) -------------------
def load_data():
    """Try to load real dataset; fallback to sample if none found."""
    # Try CSV
    if os.path.exists('data/recipes.csv'):
        df = pd.read_csv('data/recipes.csv')
        df = df[['name', 'ingredients']].copy()
    # Try Excel
    elif os.path.exists('data/recipes.xlsx'):
        df = pd.read_excel('data/recipes.xlsx')
        df = df[['name', 'ingredients']].copy()
    # Try JSON
    elif os.path.exists('data/recipes.json'):
        df = pd.read_json('data/recipes.json')
        df = df[['name', 'ingredients']].copy()
    # Fallback sample dataset (10 recipes)
    else:
        print("No external dataset found. Using sample recipes.")
        df = pd.DataFrame({
            'name': [
                'Spaghetti Aglio e Olio', 'Chicken Curry', 'Vegetable Stir Fry',
                'Pancakes', 'Tomato Soup', 'Omelette', 'Caesar Salad',
                'Fried Rice', 'Banana Bread', 'Grilled Cheese'
            ],
            'ingredients': [
                'spaghetti, garlic, olive oil, chili flakes, parsley',
                'chicken, onion, tomato, garlic, ginger, cumin, turmeric',
                'broccoli, bell pepper, carrot, soy sauce, ginger, garlic',
                'flour, milk, egg, sugar, baking powder',
                'tomato, onion, garlic, basil, cream',
                'egg, milk, cheese, salt, pepper',
                'lettuce, parmesan, croutons, caesar dressing, chicken',
                'rice, egg, peas, carrot, soy sauce, garlic',
                'banana, flour, egg, sugar, baking soda',
                'bread, cheese, butter'
            ]
        })
    return df

df = load_data()

# Clean and vectorize ingredients
df['ingredients_clean'] = df['ingredients'].fillna('').apply(lambda x: ' '.join(str(x).lower().split(',')))

vectorizer = CountVectorizer(token_pattern=r'[^\s]+', max_features=5000)
ingredient_vectors = vectorizer.fit_transform(df['ingredients_clean'])
similarity_matrix = cosine_similarity(ingredient_vectors)  # not directly used, but kept for potential expansion

def preprocess_user_ingredients(user_input):
    """Convert user input (comma-separated) into a clean string."""
    user_input = user_input.lower()
    user_input = re.sub(r'[^a-z\s,]', '', user_input)
    return ' '.join([ingredient.strip() for ingredient in user_input.split(',')])

def get_recommendations(user_ingredients_str, top_n=10):
    """Return top N recipe recommendations based on ingredient similarity."""
    user_vec = vectorizer.transform([user_ingredients_str])
    scores = cosine_similarity(user_vec, ingredient_vectors).flatten()
    # Get top N indices (excluding very low scores)
    top_indices = scores.argsort()[-top_n:][::-1]
    recommendations = []
    for idx in top_indices:
        score = scores[idx]
        if score > 0.05:  # ignore very low matches
            recommendations.append({
                'name': df.iloc[idx]['name'],
                'ingredients': df.iloc[idx]['ingredients'],
                'similarity': round(score, 3)
            })
    return recommendations

# ------------------- ROUTES -------------------
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/recommend', methods=['POST'])
def recommend():
    user_input = request.form.get('ingredients', '')
    if not user_input.strip():
        return render_template('results.html', error="Please enter some ingredients.")
    processed = preprocess_user_ingredients(user_input)
    recs = get_recommendations(processed)
    return render_template('results.html', recommendations=recs, user_input=user_input)

if __name__ == '__main__':
    app.run(debug=True)