import numpy as np
from src.model import build_model

# -------- RMSE --------
def compute_rmse():
    matrix, similarity = build_model()

    predictions = similarity.dot(matrix) / np.array([np.abs(similarity).sum(axis=1)]).T

    actual = matrix.values
    predicted = predictions

    mask = actual > 0
    mse = ((actual[mask] - predicted[mask]) ** 2).mean()
    rmse = np.sqrt(mse)

    return rmse


# -------- Precision@K --------
def precision_at_k(user_id, k=5):
    from src.recommend import get_recommendations

    matrix, _ = build_model()

    if user_id not in matrix.index:
        return 0

    recommended = get_recommendations(user_id, top_n=k)

    actual = matrix.loc[user_id]
    relevant_items = actual[actual >= 4].index

    if len(recommended) == 0:
        return 0

    relevant_recommended = [item for item in recommended if item in relevant_items]

    return len(relevant_recommended) / len(recommended)