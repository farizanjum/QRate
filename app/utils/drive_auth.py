import os
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.colab import auth
from flask import current_app

class DriveAuthenticator:
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    
    @staticmethod
    def authenticate():
        """Authenticate with Google Drive"""
        try:
            # First try Colab authentication
            try:
                auth.authenticate_user()
                current_app.logger.info("Successfully authenticated with Colab")
                return True
            except:
                current_app.logger.info("Not running in Colab, trying local authentication")
            
            creds = None
            token_path = 'token.json'
            credentials_path = 'credentials.json'  # Your downloaded credentials file

            # Check if we have valid credentials
            if os.path.exists(token_path):
                creds = Credentials.from_authorized_user_file(token_path, DriveAuthenticator.SCOPES)

            # If no valid credentials, let's get them
            if not creds or not creds.valid:
                if creds and creds.expired and creds.refresh_token:
                    creds.refresh(Request())
                else:
                    if not os.path.exists(credentials_path):
                        raise Exception("credentials.json not found")
                    
                    flow = InstalledAppFlow.from_client_secrets_file(
                        credentials_path, DriveAuthenticator.SCOPES)
                    creds = flow.run_local_server(port=0)

                # Save credentials for future use
                with open(token_path, 'w') as token:
                    token.write(creds.to_json())

            current_app.logger.info("Successfully authenticated with Google Drive")
            return True

        except Exception as e:
            current_app.logger.error(f"Error authenticating with Google Drive: {e}")
            return False 