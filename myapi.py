import requests
from textblob import TextBlob
from classifier import Classifiers as clf
import time
import os

# making API class where we'll create different methods for analysing text
class API:

    def __init__(self):

        self.api_key = os.getenv("HUGGINGFACE_API_KEY")  # Get API key from environment

        # creating an object of classifiers class and by that object we can call any method of classifiers class
        self.clfo = clf()

    def analyze_sentiment(self, text):

        # Checking if text is empty
        if not text.strip():
            return "Error: Input text is empty. Please enter text for analysis."

        blob = TextBlob(text)

        print(blob)

        # Analyze and classify sentiment of the text.
        polarity_score = blob.sentiment.polarity

        print(polarity_score)

        polarity_label = self.clfo.classify_polarity(polarity_score)

        print(polarity_label)

        return polarity_label

    def perform_NER(self, text):

        if not text.strip():
            return "Error: Input text is empty. Please enter text for analysis."

        # only if text is not empty the we'll proceed
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        # Send request to Hugging Face API (NER model)
        response = requests.post(
            'https://api-inference.huggingface.co/models/dbmdz/bert-large-cased-finetuned-conll03-english',
            headers=headers,
            json={"inputs": text}
        )

        try:
            result = response.json()  # Convert response to JSON
        except ValueError:
            return "Error: Unable to parse API response."

        # 🔹 Check if the response contains an "error" key
        if isinstance(result, dict) and "error" in result:
            return f"API Error: {result['error']}"

        # 🔹 Ensure the response is a list
        if not isinstance(result, list):
            return "Error: Unexpected response format from API."

        formatted_text = ''
        for i in result:
            # 🔹 Ensure 'word' and 'entity_group' exist in the dictionary
            if 'word' in i and 'entity_group' in i:
                formatted_text += '{} {} {} <br>'.format(
                    i['word'], "-->", self.clfo.ner_labels_full_names(i['entity_group'])
                )

        return formatted_text if formatted_text else "No named entities found."

    def get_label_full_name(self, label):
        return self.clfo.ner_labels_full_names(label)

    def analyze_emotion(self, text):

        if not text.strip():
            return "Error: Input text is empty. Please enter text for analysis."


        # """Send text for emotion analysis via API and generate a sentence based on emotion."""
        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        # Send the request to Hugging Face API for emotion detection
        response = requests.post(
            "https://api-inference.huggingface.co/models/j-hartmann/emotion-english-distilroberta-base",
            headers=headers,
            json={"inputs": text}
        )

        if response.status_code == 200:
            result = response.json()

            if isinstance(result, list) and len(result) > 0:
                # Sort emotions by score in descending order
                sorted_emotions = sorted(result[0], key=lambda x: x['score'], reverse=True)

                # Generate the sentence based on the sorted emotions
                final_response = self.clfo.generate_emotion_sentence(sorted_emotions)
            else:
                final_response = "No emotion detected or wrong response format."
        else:
            final_response = f"Error {response.status_code}: {response.text}"

        return final_response

    def detect_abuse(self, text):
        if not text.strip():
            return "Error: Input text is empty. Please enter text for analysis."

        headers = {
            'Authorization': f'Bearer {self.api_key}'
        }

        # Hugging Face model for abuse detection
        api_url = "https://api-inference.huggingface.co/models/unitary/toxic-bert"

        # Send request to Hugging Face API
        response = requests.post(api_url, headers=headers, json={"inputs": text})

        if response.status_code == 200:
            result = response.json()

            if isinstance(result, list) and len(result) > 0:
                # Sort labels by score in descending order
                sorted_labels = sorted(result[0], key=lambda x: x['score'], reverse=True)

                # Generate response based on detection
                final_response = self.clfo.generate_abuse_response(sorted_labels)
            else:
                final_response = "No abusive content detected or response format is incorrect."
        else:
            final_response = f"Error {response.status_code}: {response.text}"

        return final_response