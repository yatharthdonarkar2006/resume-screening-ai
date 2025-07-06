import streamlit as st
import tempfile
import os
import pandas as pd
from matching import rank_resumes
from utils import export_results
import pdfplumber

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file without spaCy dependency."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
    except Exception as e:
        st.error(f"Error extracting text from PDF: {e}")
        return ""
    return text.strip()

st.title('AI-Powered Resume Screening Tool')
st.success("✅ Resume screening tool is ready!")

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