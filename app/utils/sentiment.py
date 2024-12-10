from app.utils.model_manager import ModelManager
import torch
from flask import current_app

class SentimentAnalyzer:
    def __init__(self):
        try:
            self.model, self.tokenizer, self.device = ModelManager.load_model()
        except Exception as e:
            current_app.logger.error(f"Error initializing sentiment analyzer: {e}")
            raise

    def analyze(self, review_text):
        inputs = self.tokenizer(
            review_text,
            truncation=True,
            padding=True,
            max_length=128,
            return_tensors="pt"
        )
        inputs = {key: val.to(self.device) for key, val in inputs.items()}
        
        try:
            with torch.no_grad():
                outputs = self.model(**inputs)
                probabilities = torch.softmax(outputs.logits, dim=1).cpu().numpy()[0]

            positive_confidence = probabilities[1]
            negative_confidence = probabilities[0]

            if positive_confidence > 0.6:
                sentiment = "positive"
                star_rating = 5
            elif negative_confidence > 0.6:
                sentiment = "negative"
                star_rating = 1
            elif positive_confidence > negative_confidence:
                sentiment = "mixed"
                star_rating = 4 if positive_confidence > 0.4 else 3
            else:
                sentiment = "mixed"
                star_rating = 2 if negative_confidence > 0.4 else 3

            return sentiment, max(positive_confidence, negative_confidence), star_rating
            
        except Exception as e:
            current_app.logger.error(f"Error in sentiment analysis: {e}")
            raise 