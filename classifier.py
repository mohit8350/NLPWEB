class Classifiers:

    def __init__(self):
        pass

    #  classifing the intensity of emotion
    def classify_intensity(self, score):

        if score <= 0.2:
            return "slightly"
        elif score <= 0.4:
            return "moderately"
        elif score <= 0.6:
            return "highly"
        elif score <= 0.8:
            return "very"
        else:
            return "extremely"

    # Generate a sentence based on the top two emotions.
    def generate_emotion_sentence(self, emotions):

        # Sorting the emotions score in descending order
        sorted_emotions = sorted(emotions, key=lambda x: x['score'], reverse=True)

        # Get the top two emotions
        top_emotions = sorted_emotions[:2]

        # If there's a significant score difference, only take the top emotion
        score_diff = top_emotions[0]['score'] - top_emotions[1]['score']

        # Determining whether to combine the top emotions or not
        if score_diff > 0.2:
            dominant_emotion = top_emotions[0]
            emotion_label = dominant_emotion['label']
            intensity = self.classify_intensity(dominant_emotion['score'])
            sentence = f"The dominant emotion is {emotion_label}, which is {intensity} {emotion_label}."
        else:
            # Combining the emotions
            emotion_1 = top_emotions[0]
            emotion_2 = top_emotions[1]

            intensity_1 = self.classify_intensity(emotion_1['score'])
            intensity_2 = self.classify_intensity(emotion_2['score'])

            sentence = (f"The emotions are a combination of {intensity_1} {emotion_1['label']} and "
                        f"{intensity_2} {emotion_2['label']}, indicating a mix of emotions.")

        return sentence

    # Generate a sentence based on abuse detection results
    def generate_abuse_response(self, labels):
        sorted_labels = sorted(labels, key=lambda x: x['score'], reverse=True)
        top_label = sorted_labels[0]

        severity = self.classify_abuse_severity(top_label['score'])
        response = f"The text contains {severity} content classified as '{top_label['label']}'."

        return response

    # classifing polarity score into human-friendly sentiment labels.
    def classify_polarity(self, polarity):
        polarity = float(polarity)
        if polarity <= -0.75:
            return "😡 Completely Negative: The text you've provided is extremely negative! It conveys strong negativity."
        elif polarity <= -0.5:
            return "😠 Very Negative: The sentiment is highly negative. It's definitely not a positive experience."
        elif polarity <= -0.25:
            return "🙁 Slightly Negative: The text leans towards negativity, but it's not the worst."
        elif polarity < 0.05:
            return "😐 Neutral: The text seems neutral, without much emotional inclination either way."
        elif polarity <= 0.25:
            return "🙂 Slightly Positive: The sentiment is a bit positive, but it's not overwhelmingly optimistic."
        elif polarity <= 0.5:
            return "😊 Very Positive: The text is quite positive, filled with optimistic vibes."
        else:
            return "😃 Completely Positive: The text you provided is completely positive! It's full of happy and upbeat energy."

    # Classifing emotion into human-friendly labels.
    def classify_emotion(self, emotion_label):

        if emotion_label == "anger":
            return "😡 Anger: The text expresses strong feelings of anger or frustration."
        elif emotion_label == "fear":
            return "😨 Fear: The text conveys a sense of fear or anxiety."
        elif emotion_label == "joy":
            return "😊 Joy: The text is filled with happiness and excitement."
        elif emotion_label == "love":
            return "❤️ Love: The text expresses deep affection or love."
        elif emotion_label == "sadness":
            return "😢 Sadness: The text conveys feelings of sorrow or melancholy."
        elif emotion_label == "surprise":
            return "😲 Surprise: The text expresses a sense of astonishment or unexpectedness."
        elif emotion_label == "neutral":
            return "😐 Neutral: The text has no strong emotional undertones. It feels neutral."
        else:
            return "🤔 Unknown Emotion: The emotion detected is unclear or unrecognized."

    # NER labels and their full names for making it easy to understaing
    def ner_labels_full_names(self, text):

        lebels = {

            'ORG': 'Organization',
            'LOC': 'Location',
            'GPE': 'Geopolitical Entity',
            'PER': 'Person',
            'MISC': 'Miscellaneous',
            'NORP': 'Nationalities, Religions, and Political Groups',
        }
        if text in lebels:
            return lebels[text]
        else:
            return text

    # Classifying the severity of abusive content
    def classify_abuse_severity(self, score):
        if score <= 0.2:
            return "slightly abusive"
        elif score <= 0.4:
            return "moderately abusive"
        elif score <= 0.6:
            return "highly abusive"
        elif score <= 0.8:
            return "very abusive"
        else:
            return "extremely abusive"