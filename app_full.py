import streamlit as st
import tempfile
import os
import pandas as pd
from resume_parser import extract_text_from_pdf, load_spacy_model
from matching import rank_resumes
from utils import export_results

st.title('AI-Powered Resume Screening Tool')

# Check spaCy availability on first use
@st.cache_resource
def check_spacy_availability():
    """Check if spaCy model is available."""
    return load_spacy_model() is not None

# Show status based on spaCy availability
spacy_available = check_spacy_availability()
if spacy_available:
    st.success("✅ AI-powered resume screening is ready!")
else:
    st.warning("⚠️ Advanced NLP features are not available. Using basic text processing.")

job_desc = st.text_area('Paste Job Description Here')
resume_files = st.file_uploader('Upload Resume PDFs', type='pdf', accept_multiple_files=True)

if st.button('Rank Candidates'):
    if not job_desc.strip():
        st.error('Please provide a job description.')
    elif not resume_files:
        st.error('Please upload at least one resume PDF.')
    else:
        with st.spinner('Processing resumes...'):
            resumes = []
            for file in resume_files:
                try:
                    with tempfile.NamedTemporaryFile(delete=False, suffix='.pdf') as tmp:
                        tmp.write(file.read())
                        tmp_path = tmp.name
                    
                    text = extract_text_from_pdf(tmp_path)
                    if text.strip():
                        resumes.append({'name': file.name, 'text': text})
                    else:
                        st.warning(f"Could not extract text from {file.name}")
                    
                    os.unlink(tmp_path)
                except Exception as e:
                    st.error(f"Error processing {file.name}: {str(e)}")
            
            if resumes:
                try:
                    results = rank_resumes(job_desc, resumes)
                    st.success(f"Successfully ranked {len(resumes)} candidates!")
                    st.dataframe(results)
                    st.session_state['results'] = results
                except Exception as e:
                    st.error(f"Error during ranking: {str(e)}")
            else:
                st.error("No valid resumes could be processed.")

if 'results' in st.session_state:
    st.subheader("Export Results")
    col1, col2 = st.columns(2)
    with col1:
        if st.button('Export to CSV'):
            try:
                export_results(st.session_state['results'], 'ranked_candidates.csv', 'csv')
                st.success('✅ Exported to ranked_candidates.csv')
            except Exception as e:
                st.error(f"Export failed: {str(e)}")
    with col2:
        if st.button('Export to Excel'):
            try:
                export_results(st.session_state['results'], 'ranked_candidates.xlsx', 'excel')
                st.success('✅ Exported to ranked_candidates.xlsx')
            except Exception as e:
                st.error(f"Export failed: {str(e)}") 