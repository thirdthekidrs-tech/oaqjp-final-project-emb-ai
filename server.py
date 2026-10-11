
"""Flask server for the Emotion Detection application."""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector


app = Flask(__name__)


@app.route("/")
def home():
    """Display the main webpage."""
    return render_template("index.html")


@app.route("/emotionDetector")
def emotion_detector_route():
    """Detect emotions and handle invalid text."""
    text_to_analyse = request.args.get("textToAnalyze", "")

    if not text_to_analyse.strip():
        return "Invalid text! Please try again!"

    result = emotion_detector(text_to_analyse)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    return (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']}, "
        f"'disgust': {result['disgust']}, "
        f"'fear': {result['fear']}, "
        f"'joy': {result['joy']} and "
        f"'sadness': {result['sadness']}. "
        f"The dominant emotion is {result['dominant_emotion']}."
    )


if __name__ == "__main__":
    app.run(host="localhost", port=5000)
