from src.model import build_model

user_item_matrix, user_similarity = build_model()

def get_recommendations(user_id, top_n=5):
    if user_id not in user_item_matrix.index:
        return []

    user_index = user_item_matrix.index.get_loc(user_id)

    similarity_scores = list(enumerate(user_similarity[user_index]))
    similarity_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)

    similar_users = [i[0] for i in similarity_scores[1:6]]

    recommended_items = set()

    for user in similar_users:
        items = user_item_matrix.iloc[user]
        liked_items = items[items >= 4].index
        recommended_items.update(liked_items)

    # Remove already seen items
    user_items = user_item_matrix.loc[user_id]
    seen_items = user_items[user_items > 0].index

    final_recommendations = [item for item in recommended_items if item not in seen_items]

    return final_recommendations[:top_n]