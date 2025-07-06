import pdfplumber
import spacy
import subprocess
import sys
import os

def load_spacy_model():
    """Load spaCy model, downloading it if necessary."""
    try:
        return spacy.load('en_core_web_sm')
    except OSError:
        print("Downloading spaCy model 'en_core_web_sm'...")
        try:
            # Try downloading the model
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            return spacy.load('en_core_web_sm')
        except (subprocess.CalledProcessError, OSError):
            print("Failed to download spaCy model automatically.")
            # Fallback: try to use a basic model or create a simple text processor
            try:
                # Try to create a basic model without downloading
                return spacy.blank('en')
            except:
                print("Could not load any spaCy model. Using fallback text processing.")
                return None

# Initialize nlp model
nlp = load_spacy_model()

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
    if nlp is None:
        # Fallback: return basic text processing
        return text
    
    try:
        doc = nlp(text)
        return doc
    except Exception as e:
        print(f"Error processing text with spaCy: {e}")
        return text 