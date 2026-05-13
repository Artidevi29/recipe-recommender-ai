# recipe-recommender-ai
AI-powered web app that suggests recipes based on ingredients you have at home. Built with Flask, scikit-learn (cosine similarity), and Bootstrap. Uses a recipe dataset (Food.com) to find the best matches.




# 🍳 Kitchen Chef AI – Recipe Recommender

[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-green)](https://flask.palletsprojects.com)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.1-orange)](https://scikit-learn.org)
[![License](https://img.shields.io/badge/License-MIT-yellow)](LICENSE)

**An AI-powered web app that suggests recipes based on ingredients you have at home.**  
Simply type in what's in your kitchen, and the system finds the best matching recipes using **cosine similarity**.

🔗 **Live Demo**: *[Add your Render or Streamlit URL after deployment]*

---

## ✨ Features

- 🔍 **Ingredient‑based search** – enter any combination of ingredients (e.g., `chicken, rice, tomato`).
- 🤖 **AI matching** – uses `CountVectorizer` and `cosine similarity` from scikit-learn.
- 🍲 **Thousands of recipes** – works with the popular Food.com dataset (or your own).
- ⚡ **Fast & lightweight** – runs locally or in the cloud.
- 📱 **Responsive design** – works on desktop, tablet, and mobile (Bootstrap 5).
- 🧪 **Fallback sample data** – no dataset? The app includes 10 example recipes to test immediately.

---

## 🛠️ Tech Stack

| Layer          | Technology                               |
|----------------|------------------------------------------|
| Backend        | Flask (Python)                           |
| Recommendation | scikit-learn (CountVectorizer, cosine_similarity) |
| Data handling  | Pandas, NumPy                            |
| Frontend       | HTML, Bootstrap 5, Jinja2 templates      |
| Deployment     | Render (or any PaaS)                     |

---

