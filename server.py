
"""Flask server for the Emotion Detection application."""

from flask import Flask, request, render_template
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Display the home page."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Process the user's text and display emotion results."""
    text_to_analyse = request.args.get("textToAnalyze")

    result = emotion_detector(text_to_analyse)

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is "
        f"{result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
