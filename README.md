# 🎯 Movie Recommender System

## 🔥 Key Highlights

* Personalized movie recommendations using collaborative filtering  
* Uses cosine similarity for accurate recommendations  
* Recommends top-N similar movies  
* Evaluated using RMSE and Precision@K  
* Interactive UI built with Streamlit  

---

## 📌 Overview

This project is a **movie recommendation system** that suggests movies to users based on their preferences. It uses **collaborative filtering techniques** to find similarities between users or items and recommend relevant movies.

The system analyzes user ratings and identifies patterns to provide **personalized recommendations**.

---

## 🚀 Features

* 🎬 Personalized movie recommendations  
* 📊 Similarity-based filtering (cosine similarity)  
* ⭐ Top-N recommendations  
* 📈 Evaluation using RMSE & Precision@K  
* 🌐 Interactive UI with Streamlit  

---

## 🛠️ Tech Stack

* Python  
* Pandas  
* NumPy  
* Scikit-learn  
* Streamlit  

---

## ⚙️ Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/sanjanach-04/object-detection.git
cd object-detection
```

### 2️⃣ Create virtual environment

```bash
python -m venv venv
```

### 3️⃣ Activate environment

```bash
venv\Scripts\activate   # Windows
source venv/bin/activate  # Mac/Linux
```

### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

```bash
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000/
```

---

🧠 How It Works

User selects or inputs a movie

System finds similar movies using cosine similarity

Movies are ranked based on similarity score

Top-N recommended movies are displayed

📊 Dataset

The system uses a movie dataset containing:

Movie titles

User ratings

Movie metadata

⚠️ Challenges Faced

Data sparsity (few ratings per user)

Cold start problem for new users/movies

Limited recommendations due to filtering conditions

🔮 Future Improvements

Hybrid recommendation (content + collaborative)

Handle cold start problem effectively

Add user authentication and profiles

Deploy using cloud platforms

📸 Demo
📸 Demo Output
<p align="center"> <img src="demo1.png" width="600"/> </p> <p align="center"> <img src="demo2.png" width="600"/> </p> <p align="center"> <img src="demo3.png" width="600"/> </p>
📌 Resume Description

Developed a movie recommendation system using collaborative filtering and cosine similarity to provide personalized recommendations, evaluated using RMSE and Precision@K, and deployed with a Streamlit interface.
