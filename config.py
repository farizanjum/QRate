import os
from dotenv import load_dotenv

# Only load .env file in development
if not os.environ.get('RENDER'):
    load_dotenv()

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your-secret-key-here'
    SMTP_SERVER = "smtp.gmail.com"
    SMTP_PORT = 587
    SENDER_EMAIL = os.environ.get('SENDER_EMAIL')
    SENDER_PASSWORD = os.environ.get('SENDER_PASSWORD')
    RECIPIENT_EMAIL = os.environ.get('RECIPIENT_EMAIL')
    
    # Google OAuth credentials
    GOOGLE_OAUTH_CLIENT_ID = os.environ.get('GOOGLE_OAUTH_CLIENT_ID')
    GOOGLE_OAUTH_CLIENT_SECRET = os.environ.get('GOOGLE_OAUTH_CLIENT_SECRET')
    GOOGLE_CLOUD_PROJECT_ID = os.environ.get('GOOGLE_CLOUD_PROJECT_ID')
    
    # Determine if we're running on Render
    IS_PRODUCTION = os.environ.get('RENDER') is not None
    
    # OAuth redirect URI based on environment
    OAUTH_REDIRECT_URI = (
        f"https://{os.environ.get('RENDER_EXTERNAL_URL')}/oauth2callback"
        if IS_PRODUCTION else
        "http://localhost:5000/oauth2callback"
    )
