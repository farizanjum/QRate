# QRate - AI-Powered Customer Feedback System

QRate is an intelligent feedback collection and analysis system that uses AI to process customer feedback in real-time.

## Features

- **AI-Powered Sentiment Analysis**: Uses fine-tuned DistilBERT model for accurate sentiment classification
- **Multi-Language Support**: Available in English, Hindi, and Urdu
- **Real-time Email Notifications**: Instant feedback alerts with sentiment analysis
- **Google Reviews Integration**: Seamless redirection for positive feedback
- **Mobile Responsive Design**: Works perfectly on all devices

## Tech Stack

- **Backend**: Flask
- **ML Model**: DistilBERT (PyTorch)
- **Frontend**: HTML, CSS, JavaScript
- **Email**: SMTP
- **Deployment**: ngrok for tunneling

## Setup

1. Clone the repository:
    ```bash
    git clone https://github.com/farizanjum/QRate.git
    cd QRate
    ```

2. Create and configure credentials:
    ```bash
    # Copy the credentials template
    cp credentials.json.example credentials.json
    
    # Edit credentials.json with your actual Google OAuth credentials
    # Get these from Google Cloud Console
    ```

3. Set up environment variables:
    ```bash
    # Copy the environment template
    cp .env.example .env
    
    # Edit .env with your actual values
    ```

4. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. Run the application:
    ```bash
    python app.py
    ```

2. Access the application in your browser at:
    ```
    http://localhost:5000
    ```

## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes
4. Commit your changes
5. Push to the branch
6. Create a pull request

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.