import torch
from transformers import DistilBertTokenizer, DistilBertForSequenceClassification
from flask import current_app

class ModelManager:
    @staticmethod
    def load_model():
        """Load the model and tokenizer"""
        try:
            # Use pre-trained model from Hugging Face
            model_name = "distilbert-base-uncased-finetuned-sst-2-english"
            
            model = DistilBertForSequenceClassification.from_pretrained(model_name)
            tokenizer = DistilBertTokenizer.from_pretrained(model_name)
            
            device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
            model.to(device)
            model.eval()
            
            return model, tokenizer, device
            
        except Exception as e:
            current_app.logger.error(f"Error loading model: {e}")
            raise 