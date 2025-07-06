# Deployment Guide

## Quick Deployment to Streamlit Cloud

### Step 1: Prepare Your Repository

1. **Initialize Git** (if not already done):
   ```bash
   git init
   git add .
   git commit -m "Initial commit"
   ```

2. **Create GitHub Repository**:
   - Go to [GitHub](https://github.com)
   - Create a new repository
   - Follow the instructions to push your code

3. **Push to GitHub**:
   ```bash
   git remote add origin https://github.com/yourusername/resume-screening-ai.git
   git branch -M main
   git push -u origin main
   ```

### Step 2: Deploy to Streamlit Cloud

1. **Go to Streamlit Cloud**:
   - Visit [share.streamlit.io](https://share.streamlit.io)
   - Sign in with your GitHub account

2. **Connect Repository**:
   - Click "New app"
   - Select your repository
   - Set the main file path to `app.py`
   - Click "Deploy"

3. **Wait for Deployment**:
   - Streamlit will automatically install dependencies
   - The spaCy model will be downloaded automatically
   - Your app will be available at `https://your-app-name.streamlit.app`

### Step 3: Verify Deployment

1. **Check the App**:
   - Open your deployed app URL
   - You should see a success message: "✅ AI-powered resume screening is ready!"
   - If you see a warning, the app will still work with basic processing

2. **Test the App**:
   - Upload a PDF resume
   - Paste a job description
   - Click "Rank Candidates"
   - Verify the results are displayed correctly

## Troubleshooting

### Common Issues

1. **spaCy Model Error**:
   - The app includes fallback processing
   - It will work even without the full spaCy model
   - Check the status message at the top of the app

2. **Upload Issues**:
   - Ensure PDF files are valid
   - Check file size (max 200MB)
   - Try with different PDF files

3. **Deployment Fails**:
   - Check that all files are committed to GitHub
   - Verify `requirements.txt` is in the root directory
   - Ensure `app.py` is the main file

### Files Included for Deployment

- ✅ `app.py` - Main Streamlit application
- ✅ `resume_parser.py` - PDF processing with fallback
- ✅ `matching.py` - AI ranking logic
- ✅ `utils.py` - Export functionality
- ✅ `requirements.txt` - Python dependencies
- ✅ `packages.txt` - System dependencies
- ✅ `.streamlit/config.toml` - Streamlit configuration
- ✅ `setup_spacy.py` - Model installation helper

## Support

If you encounter issues:
1. Check the Streamlit Cloud logs
2. Verify all files are properly committed
3. Try redeploying the app
4. Open an issue on GitHub with error details 