import pdfplumber
import spacy
import subprocess
import sys
import os

# Global variable to store the loaded model
_nlp_model = None

def load_spacy_model():
    """Load spaCy model, downloading it if necessary."""
    global _nlp_model
    if _nlp_model is not None:
        return _nlp_model
    
    try:
        _nlp_model = spacy.load('en_core_web_sm')
        return _nlp_model
    except OSError:
        print("Downloading spaCy model 'en_core_web_sm'...")
        try:
            # Try downloading the model
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            _nlp_model = spacy.load('en_core_web_sm')
            return _nlp_model
        except (subprocess.CalledProcessError, OSError):
            print("Failed to download spaCy model automatically.")
            # Fallback: try to use a basic model or create a simple text processor
            try:
                # Try to create a basic model without downloading
                _nlp_model = spacy.blank('en')
                return _nlp_model
            except:
                print("Could not load any spaCy model. Using fallback text processing.")
                _nlp_model = None
                return None

def extract_text_from_pdf(pdf_path):
    """Extract text from PDF file."""
    text = ""
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                text += page_text + "\n"
    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        return ""
    return text.strip()

def parse_resume(text):
    """Parse resume text using spaCy or fallback processing."""
    nlp = load_spacy_model()
    if nlp is None:
        # Fallback: return basic text processing
        return text
    
    try:
        doc = nlp(text)
        return doc
    except Exception as e:
        print(f"Error processing text with spaCy: {e}")
        return text 