from transformers import pipeline
import numpy as np

# Load models
sentiment_model = pipeline("sentiment-analysis", model="distilbert-base-uncased-finetuned-sst-2-english")
emotion_model = pipeline("text-classification", model="bhadresh-savani/distilbert-base-uncased-emotion", top_k=None)
toxicity_model = pipeline("text-classification", model="unitary/unbiased-toxic-roberta", top_k=None)

def analyze_text(text):
    """
    Analyzes sentiment, emotions, and toxicity.
    Returns:
    - Sentiment Score
    - Sentiment Label
    - Emotion Breakdown
    - Toxicity Score
    - Toxicity Label
    """
    try:
        # Sentiment Analysis
        sentiment_result = sentiment_model(text)[0]
        sentiment_score = sentiment_result['score']
        sentiment_label = sentiment_result['label']
        
        # Emotion Analysis - Normalize values
        emotion_result = emotion_model(text)[0]
        emotion_scores = {entry["label"]: entry["score"] for entry in emotion_result}
        total_emotion = sum(emotion_scores.values())
        if total_emotion > 0:
            emotion_scores = {k: v / total_emotion for k, v in emotion_scores.items()}  # Normalize emotions
        emotion_scores = {k: v for k, v in emotion_scores.items() if v > 0.01}  # Remove insignificant values
        
        # Toxicity Analysis - Adjust threshold
        toxicity_result = toxicity_model(text)[0]
        toxicity_scores = {entry["label"]: entry["score"] for entry in toxicity_result}
        toxicity_score = max(toxicity_scores.values(), default=0.0)
        toxicity_label = "Safe" if toxicity_score < 0.4 else "Toxic"  # Adjusted threshold
        
        return sentiment_score, sentiment_label, emotion_scores, toxicity_score, toxicity_label
    
    except Exception as e:
        print(f"Error processing text: {e}")
        return 0.0, "Neutral", {}, 0.0, "Safe"

# Example test
if __name__ == "__main__":
    sample_texts = [
        "Darth Vader loves to destroy planets!",
        "I hate how this is happening.",
        "I absolutely love this product!",
        "This is the worst experience I've had.",
        "Oh great, another delay...",
        "You are so dumb and worthless!",
    ]
    
    for text in sample_texts:
        sentiment_score, sentiment_label, emotions, toxicity_score, toxicity_label = analyze_text(text)
        print(f"Text: {text}\nSentiment Score: {sentiment_score}, Label: {sentiment_label}")
        print(f"Toxicity Score: {toxicity_score}, Label: {toxicity_label}")
        print(f"Emotions: {emotions}\n")
