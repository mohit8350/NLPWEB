# NLP Web App

## Overview

This is a Flask-based web application that provides various NLP (Natural Language Processing) functionalities using Hugging Face models. The application allows users to perform tasks such as Named Entity Recognition (NER), Sentiment Analysis, Emotion Detection, and Abuse Detection.

## Features

- **User Authentication**: Registration and login system with email and password.
- **Named Entity Recognition (NER)**: Detects and classifies named entities (persons, organizations, locations, etc.).
- **Sentiment Analysis**: Determines the sentiment (positive, neutral, or negative) of a given text.
- **Emotion Analysis**: Identifies emotions such as joy, sadness, anger, and love in text.
- **Abuse Detection**: Detects toxic or abusive content in text.

## Installation

### Prerequisites

- Python 3.8+
- Flask
- Requests
- TextBlob

### Setup

1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/NLPWEB.git
   cd NLPWEB
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up Hugging Face API Key:
   - Create a `.env` file in the project root and add:
     ```sh
     HUGGINGFACE_API_KEY=your_huggingface_api_key
     ```
4. Run the Flask application:
   ```sh
   python web_app.py
   ```
5. Open the app in your browser at `http://127.0.0.1:5000/`.

## File Structure

```
NLPWEB
|- templates/            # HTML templates for Flask app
|- static/               # Static files (CSS, JS, images)
|- classifier.py         # Contains classification logic
|- myapi.py             # API wrapper for NLP models
|- mydb.json            # Local database for user authentication
|- mydb_code.py         # Handles user authentication
|- web_app.py           # Flask application
```

## API Endpoints

### User Authentication

- `/` - Login page
- `/register` - Registration page
- `/perform_login` - Processes login requests
- `/perform_registration` - Processes registration requests

### NLP Functionalities

- `/home` - Home page
- `/ner` - Named Entity Recognition page
- `/perform_ner` - Performs NER on input text
- `/sentiment_analysis` - Sentiment Analysis page
- `/perform_sentiment_analysis` - Performs sentiment analysis
- `/emotion_analysis` - Emotion Analysis page
- `/perform_emotion_analysis` - Performs emotion analysis
- `/abuse_detection` - Abuse Detection page
- `/perform_abuse_detection` - Detects abuse in input text

## Technologies Used

- **Flask** - Web framework
- **Hugging Face Transformers** - NLP models
- **TextBlob** - Sentiment analysis
- **HTML/CSS/JavaScript** - Frontend development

## Future Improvements

- Improve UI with better styling
- Add a database for storing analysis history
- Implement additional NLP models

##

