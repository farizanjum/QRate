import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from flask import current_app
import os

class ModelManager:
    @staticmethod
    def load_model():
        """Load the model and tokenizer"""
        try:
            model_name = "distilbert-base-uncased-finetuned-sst-2-english"
            model = DistilBertForSequenceClassification.from_pretrained(model_name)
            tokenizer = DistilBertTokenizer.from_pretrained(model_name)
            
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)
            model.eval()
            
            # Load credentials from environment variables
            client_id = os.getenv("GOOGLE_OAUTH_CLIENT_ID")
            client_secret = os.getenv("GOOGLE_OAUTH_CLIENT_SECRET")
            project_id = os.getenv("GOOGLE_CLOUD_PROJECT_ID")
            
            return model, tokenizer, device
            
        except Exception as e:
            current_app.logger.error(f"Error loading model: {e}")
            raise
