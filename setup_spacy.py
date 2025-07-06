#!/usr/bin/env python3
"""
Setup script for spaCy model installation.
This script ensures the spaCy model is properly installed in the deployment environment.
"""

import subprocess
import sys
import os

def install_spacy_model():
    """Install spaCy model if not already installed."""
    try:
        import spacy
        # Try to load the model
        nlp = spacy.load('en_core_web_sm')
        print("✅ spaCy model 'en_core_web_sm' is already installed.")
        return True
    except OSError:
        print("📥 Installing spaCy model 'en_core_web_sm'...")
        try:
            subprocess.check_call([
                sys.executable, "-m", "spacy", "download", "en_core_web_sm"
            ])
            print("✅ spaCy model installed successfully!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to install spaCy model: {e}")
            return False

if __name__ == "__main__":
    success = install_spacy_model()
    if success:
        print("🎉 Setup completed successfully!")
    else:
        print("⚠️  Setup completed with warnings. The app will use fallback processing.") 