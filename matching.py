from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd
import re

def preprocess_text(text):
    """Basic text preprocessing without spaCy."""
    if not text:
        return ""
    
    # Convert to lowercase
    text = text.lower()
    
    # Remove special characters but keep spaces
    text = re.sub(r'[^\w\s]', ' ', text)
    
    # Remove extra whitespace
    text = re.sub(r'\s+', ' ', text).strip()
    
    return text

def rank_resumes(job_description, resumes):
    """Rank resumes based on similarity to job description."""
    if not job_description.strip():
        raise ValueError("Job description cannot be empty")
    
    if not resumes:
        raise ValueError("No resumes provided")
    
    # Preprocess job description
    processed_job_desc = preprocess_text(job_description)
    
    # Preprocess resumes
    processed_resumes = []
    valid_resumes = []
    
    for resume in resumes:
        processed_text = preprocess_text(resume['text'])
        if processed_text.strip():  # Only include non-empty resumes
            processed_resumes.append(processed_text)
            valid_resumes.append(resume)
    
    if not valid_resumes:
        raise ValueError("No valid resumes found after preprocessing")
    
    # Create documents list for vectorization
    documents = [processed_job_desc] + processed_resumes
    
    # Create TF-IDF vectors
    try:
        vectorizer = TfidfVectorizer(
            stop_words='english',
            max_features=5000,
            ngram_range=(1, 2)
        )
        tfidf_matrix = vectorizer.fit_transform(documents)
        
        # Calculate similarities
        job_vec = tfidf_matrix[0]
        resume_vecs = tfidf_matrix[1:]
        similarities = cosine_similarity(job_vec, resume_vecs).flatten()
        
        # Create results dataframe
        results = pd.DataFrame({
            'Candidate': [r['name'] for r in valid_resumes],
            'Score': similarities,
            'Match Percentage': [f"{score * 100:.1f}%" for score in similarities]
        })
        
        # Sort by score (descending)
        results = results.sort_values(by='Score', ascending=False).reset_index(drop=True)
        
        return results
        
    except Exception as e:
        print(f"Error in ranking process: {e}")
        # Fallback: return basic results
        results = pd.DataFrame({
            'Candidate': [r['name'] for r in valid_resumes],
            'Score': [0.5] * len(valid_resumes),  # Default score
            'Match Percentage': ['50.0%'] * len(valid_resumes)
        })
        return results 