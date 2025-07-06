import subprocess
import sys

def install_spacy_model():
    """Install the required spaCy model."""
    try:
        subprocess.check_call([
            sys.executable, "-m", "spacy", "download", "en_core_web_sm"
        ])
        print("✅ spaCy model 'en_core_web_sm' installed successfully!")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error installing spaCy model: {e}")
        sys.exit(1)

if __name__ == "__main__":
    install_spacy_model() 