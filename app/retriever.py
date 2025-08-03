from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from app.loader import load_documents

#TF-IDF based simple retriever for markdown
class Retriever:
    def __init__(self):
        #load documents
        self.docs = load_documents()
        self.doc_names = [doc[0] for doc in self.docs]
        self.contents = [doc[1] for doc in self.docs]

        #vectorize documents using TF-IDF
        self.vectorizer = TfidfVectorizer(stop_words="english")
        self.doc_vectors = self.vectorizer.fit_transform(self.contents)

    #returns top K docs relevant to the query
    def get_top_docs(self, query: str, top_k: int = 3) -> list[dict]:
        q_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(q_vec, self.doc_vectors).flatten()
        top_indices = scores.argsort()[::-1][:top_k]
        max_score = scores[top_indices[0]] if top_indices.size > 0 else 0
        return [
            {
                "doc": self.doc_names[i],
                #show first 300 characters
                "snippet": self.contents[i][:300],
                "score": scores[i],
                "max_score": max_score
            }
            for i in top_indices if scores[i] > 0.05
        ]
