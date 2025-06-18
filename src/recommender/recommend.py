
import json
import pandas as pd
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class UserRecommender:
    def __init__(self, load_from_file=True, file_path="dummyUsers.json"):
        self.file_path = file_path
        self.model = SentenceTransformer("all-MiniLM-L6-v2")
        self.user_data = []
        self.df_users = pd.DataFrame()
        self.embeddings = None
        self.user_id_to_index = {}

        if load_from_file:
            self.load_data()

    def load_data(self):
        with open(self.file_path, "r") as f:
            self.user_data = json.load(f)
        self._build_dataframe_and_cache()

    def _build_dataframe_and_cache(self):
        self.df_users = pd.DataFrame(self.user_data)
        self.df_users["features"] = self.df_users["skills"].apply(lambda x: " ".join(x)) + " " + self.df_users["interests"].apply(lambda x: " ".join(x))
        self.embeddings = self.model.encode(self.df_users["features"].tolist(), show_progress_bar=False)
        self.user_id_to_index = {user["user_id"]: idx for idx, user in enumerate(self.user_data)}

    def recommend_users(self, user_id: str, top_n: int = 5):
        if user_id not in self.user_id_to_index:
            return []

        user_idx = self.user_id_to_index[user_id]
        user_embedding = self.embeddings[user_idx].reshape(1, -1)
        sim_scores = cosine_similarity(user_embedding, self.embeddings).flatten()

        similar_indices = np.argsort(-sim_scores)
        recommended = [self.user_data[i] for i in similar_indices if i != user_idx][:top_n]
        return recommended

    def add_user(self, user_id, skills, interests):
        new_user = {
            "user_id": user_id,
            "skills": skills,
            "interests": interests
        }
        feature = " ".join(skills) + " " + " ".join(interests)
        new_embedding = self.model.encode([feature])[0]

        self.user_data.append(new_user)
        new_row = pd.DataFrame([{
            "user_id": user_id,
            "skills": skills,
            "interests": interests,
            "features": feature
        }])
        self.df_users = pd.concat([self.df_users, new_row], ignore_index=True)
        self.embeddings = np.vstack([self.embeddings, new_embedding]) if self.embeddings is not None else np.array([new_embedding])
        self.user_id_to_index[user_id] = len(self.user_data) - 1
        return True

# Example usage
if __name__ == "__main__":
    recommender = UserRecommender(load_from_file=True)
    recommender.add_user("u301", ["React", "Flask"], ["Web Development"])
    recs = recommender.recommend_users("u79", 10)
    print(f"Recommendations for u301:\n")
    for r in recs:
        print(r)
