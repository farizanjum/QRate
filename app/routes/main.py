from flask import Blueprint, render_template, request, current_app
from app.utils.sentiment import SentimentAnalyzer
from app.utils.email import send_feedback_email

bp = Blueprint('main', __name__)
sentiment_analyzer = None

@bp.before_app_request
def initialize_analyzer():
    global sentiment_analyzer
    if sentiment_analyzer is None:
        sentiment_analyzer = SentimentAnalyzer()

@bp.route('/')
def home():
    return render_template('home.html')

@bp.route('/feedback', methods=['GET', 'POST'])
def feedback():
    if request.method == 'POST':
        try:
            name = request.form.get('name', '').strip()
            mobile = request.form.get('mobile', '').strip()
            feedback_text = request.form.get('feedback', '').strip()

            # Validation
            if not mobile or not feedback_text:
                return "<script>alert('Please fill out all required fields!'); window.history.back();</script>"
            
            if not mobile.isdigit() or len(mobile) < 10:
                return "<script>alert('Please enter a valid mobile number!'); window.history.back();</script>"
            
            if len(feedback_text) < 5:
                return "<script>alert('Please provide more detailed feedback!'); window.history.back();</script>"

            # Sentiment Analysis
            sentiment, confidence, star_rating = sentiment_analyzer.analyze(feedback_text)
            
            # Send Email
            if send_feedback_email(name, mobile, feedback_text, sentiment, confidence, star_rating):
                return render_template('thank_you.html', rating=star_rating)
            else:
                current_app.logger.error("Failed to send feedback email")
                return render_template('error.html', message="Unable to process feedback")

        except Exception as e:
            current_app.logger.error(f"Error processing feedback: {e}")
            return render_template('error.html', message="Internal Server Error"), 500

    return render_template('feedback.html')
