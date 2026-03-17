import streamlit as st
import pandas as pd
from src.recommend import get_recommendations
from src.evaluate import compute_rmse, precision_at_k

# -------------------- PAGE CONFIG --------------------
st.set_page_config(
    page_title="Recommender System",
    page_icon="🎯",
    layout="wide"
)

# -------------------- TITLE --------------------
st.title("🎯 Recommender System")
st.markdown("### Personalized Movie Recommendations System")

# -------------------- LOAD DATA --------------------
@st.cache_data
def load_data():
    ratings = pd.read_csv("data/ratings.csv")
    movies = pd.read_csv("data/movies.csv")
    return ratings, movies

ratings, movies = load_data()

# -------------------- HELPER FUNCTION --------------------
def get_movie_name(movie_id):
    result = movies[movies["movieId"] == movie_id]["title"]
    return result.values[0] if not result.empty else f"Movie {movie_id}"

# -------------------- SIDEBAR --------------------
st.sidebar.header("⚙️ Options")

user_list = sorted(ratings["userId"].unique())
user_id = st.sidebar.selectbox("Select User ID", user_list)

top_n = st.sidebar.slider("Number of Recommendations", 1, 10, 5)

# -------------------- MAIN BUTTON --------------------
if st.button("🚀 Get Recommendations"):
    recommendations = get_recommendations(user_id, top_n=top_n)

    st.subheader("🎬 Recommended Movies")

    if recommendations:
        for i, item in enumerate(recommendations, 1):
            st.write(f"{i}. 👉 {get_movie_name(item)}")
    else:
        st.warning("No recommendations found for this user")

# -------------------- METRICS SECTION --------------------
st.markdown("---")
st.subheader("📊 Evaluation Metrics")

col1, col2 = st.columns(2)

# RMSE
with col1:
    if st.checkbox("Show RMSE"):
        rmse = compute_rmse()
        st.metric(label="RMSE", value=f"{rmse:.4f}")
        st.caption("Lower RMSE → better prediction accuracy")

# Precision@K
with col2:
    if st.checkbox("Show Precision@K"):
        precision = precision_at_k(user_id, k=top_n)
        st.metric(label="Precision@K", value=f"{precision:.2f}")
        st.caption("Higher Precision → better recommendation relevance")

# -------------------- INFO SECTION --------------------
st.markdown("---")
st.subheader("ℹ️ About This Project")

st.markdown("""
This recommender system is based on:

- **User-Based Collaborative Filtering**
- **Cosine Similarity**
- **User-Item Matrix Representation**

### Key Concepts:
- Similar users have similar preferences
- Recommendations are generated from nearest neighbors
- Evaluated using RMSE and Precision@K

### Challenges:
- Cold Start Problem  
- Data Sparsity  
- Scalability  

### Future Improvements:
- Matrix Factorization (SVD)
- Deep Learning Recommenders
""")

# -------------------- FOOTER --------------------
st.markdown("---")
st.markdown("Built with ❤️ using Streamlit | AIML Project")