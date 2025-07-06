from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

def rank_resumes(job_description, resumes):
    # resumes: list of dicts with 'name' and 'text'
    documents = [job_description] + [r['text'] for r in resumes]
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(documents)
    job_vec = tfidf_matrix[0]
    resume_vecs = tfidf_matrix[1:]
    similarities = cosine_similarity(job_vec, resume_vecs).flatten()
    results = pd.DataFrame({
        'Candidate': [r['name'] for r in resumes],
        'Score': similarities
    })
    results = results.sort_values(by='Score', ascending=False).reset_index(drop=True)
    return results 