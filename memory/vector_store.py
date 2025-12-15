from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

class SimpleVectorStore:
    def __init__(self):
        self.documents = []
        self.vectorizer = TfidfVectorizer()
        self.vectors = None

    def add(self, text):
        self.documents.append(text)
        self.vectors = self.vectorizer.fit_transform(self.documents)

    def search(self, query, top_k=3):
        if not self.documents:
            return []
        query_vec = self.vectorizer.transform([query])
        scores = cosine_similarity(query_vec, self.vectors)[0]
        ranked = sorted(
            zip(self.documents, scores),
            key=lambda x: x[1],
            reverse=True
        )
        return ranked[:top_k]
