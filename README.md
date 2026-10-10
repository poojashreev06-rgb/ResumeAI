# ResumeAI — AI-Powered Resume Screening System

## Project Overview

ResumeAI is a web-based application that analyzes PDF resumes against a job description. It identifies matched and missing skills and uses Natural Language Processing (NLP) to calculate semantic similarity between the resume and job description.

## Features

* Upload resumes in PDF format.
* Extract text from resumes.
* Identify matched skills and missing skills.
* Calculate a required skill keyword match percentage.
* Calculate semantic similarity using a pretrained Sentence Transformer model.
* Display analysis results through an interactive web interface.

## Technologies Used

* Python
* Streamlit
* PyMuPDF
* Sentence Transformers
* Scikit-learn
* Natural Language Processing (NLP)

## How It Works

1. Upload a resume in PDF format.
2. Paste the job description.
3. Extract text from the resume.
4. Compare supported skill keywords against the resume.
5. Generate text embeddings using the pretrained `all-MiniLM-L6-v2` model.
6. Calculate and display skill matching and semantic similarity results.

## Installation and Setup

Clone the repository:

```bash
git clone https://github.com/poojashreev06-rgb/ResumeAI.git
cd ResumeAI
```

Install the required dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
streamlit run app.py
```

## Live Demo

[Launch ResumeAI](https://resumeai-j89mzzefeh8z24a9bpwjkw.streamlit.app)

## Limitations

The skill matcher checks a predefined list of keywords. Semantic similarity measures textual similarity and is not a hiring probability or proof of candidate proficiency. Scanned PDFs without selectable text may require OCR support.

## Future Enhancements

* Expand the supported skills list.
* Add support for additional document formats.
* Improve skill extraction and matching.
* Add visual summaries of analysis results.

## Author

**Pooja Shree V**
BCA Data Science
