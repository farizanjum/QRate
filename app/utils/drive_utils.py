from google.colab import drive
import os

def mount_drive():
    """Mount Google Drive and return the model path"""
    try:
        drive.mount('/content/drive')
        model_path = "/content/drive/MyDrive/distilbert_model"
        if not os.path.exists(model_path):
            raise Exception("Model path not found in Google Drive")
        return model_path
    except Exception as e:
        print(f"Error mounting Google Drive: {e}")
        return None 