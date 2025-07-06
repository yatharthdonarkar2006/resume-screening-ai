# AI-Powered Resume Screening Tool

An intelligent resume screening application that uses AI to rank job candidates based on their resumes against a job description.

## Features

- **PDF Resume Processing**: Upload and extract text from multiple PDF resumes
- **AI-Powered Matching**: Uses TF-IDF vectorization and cosine similarity to match resumes to job descriptions
- **Ranked Results**: Automatically ranks candidates by relevance score
- **Export Options**: Export results to CSV or Excel format
- **User-Friendly Interface**: Built with Streamlit for easy web-based interaction

## Installation

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/resume-screening-ai.git
   cd resume-screening-ai
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download spaCy model**
   ```bash
   python -m spacy download en_core_web_sm
   ```

### Streamlit Cloud Deployment

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Initial commit"
   git push origin main
   ```

2. **Deploy to Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Connect your repository
   - Deploy the app

3. **The app will automatically handle spaCy model installation**

**Note:** The app includes fallback processing if spaCy model installation fails, so it will work even without the full NLP features.

## Usage

1. **Run the application**
   ```bash
   streamlit run app.py
   ```

2. **Open your browser**
   Navigate to `http://localhost:8501`

3. **Use the application**
   - Paste a job description in the text area
   - Upload one or more resume PDFs
   - Click "Rank Candidates" to get results
   - Export results to CSV or Excel as needed

## How it Works

1. **Text Extraction**: Uses `pdfplumber` to extract text from uploaded PDF resumes
2. **NLP Processing**: Processes text using spaCy for natural language understanding
3. **Vectorization**: Converts job description and resumes to TF-IDF vectors
4. **Similarity Scoring**: Calculates cosine similarity between job description and each resume
5. **Ranking**: Ranks candidates by similarity score (higher = better match)

## Project Structure

```
resume-screening-ai/
├── app.py              # Main Streamlit application
├── resume_parser.py    # PDF text extraction and NLP processing
├── matching.py         # AI matching and ranking logic
├── utils.py           # Utility functions for data export
├── requirements.txt   # Python dependencies
└── README.md         # This file
```

## Dependencies

- **Streamlit**: Web application framework
- **spaCy**: Natural language processing
- **scikit-learn**: Machine learning algorithms
- **pandas**: Data manipulation
- **pdfplumber**: PDF text extraction
- **openpyxl**: Excel file support

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Future Enhancements

- [ ] Extract specific skills, experience, and education from resumes
- [ ] Support for more file formats (DOCX, TXT)
- [ ] Advanced NLP features (named entity recognition, skill extraction)
- [ ] Machine learning model training on historical data
- [ ] Integration with job boards and ATS systems
- [ ] Multi-language support

## Support

If you encounter any issues or have questions, please open an issue on GitHub.

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.28+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg) 