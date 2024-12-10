import smtplib
from flask import current_app

def send_feedback_email(name, mobile, feedback, sentiment, confidence, star_rating):
    try:
        smtp_server = current_app.config['SMTP_SERVER']
        smtp_port = current_app.config['SMTP_PORT']
        sender_email = current_app.config['SENDER_EMAIL']
        sender_password = current_app.config['SENDER_PASSWORD']
        recipient_email = current_app.config['RECIPIENT_EMAIL']

        subject = f"Customer Feedback ({sentiment.capitalize()}) - {star_rating}⭐"
        body = (
            f"Customer Feedback Details:\n"
            f"------------------------\n"
            f"Name: {name}\n"
            f"Mobile: {mobile}\n"
            f"Feedback: {feedback}\n\n"
            f"Analysis Results:\n"
            f"----------------\n"
            f"Sentiment: {sentiment}\n"
            f"Confidence: {confidence:.2f}\n"
            f"Star Rating: {'⭐' * star_rating}\n"
        )
        message = f"Subject: {subject}\n\n{body}"

        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            server.sendmail(sender_email, recipient_email, message)
            current_app.logger.info(f"Feedback email sent successfully for {mobile}")
        return True
    except Exception as e:
        current_app.logger.error(f"Error sending email: {e}")
        return False 