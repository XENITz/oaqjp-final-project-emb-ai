"""Flask server for emotion detection application."""
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    """
    Analyze emotion in text and return formatted response.
    Returns:
        str: Formatted string containing emotion analysis results
    """
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    # Create the return statement
    answer = "For the given statement, the system response is\n"
    for emotion, value in response.items():
        if emotion != "dominant_emotion":
            answer += f"{emotion}: {value}\n"
        else:
            if value == "None":
                answer = "Invalid text! Please try again!."
            else:
                answer += f"The dominant emotion is: {value}"
    return answer

@app.route("/")
def render_index_page():
    """
    Render the main page of the application.
    Returns:
        str: Rendered HTML template
    """
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
