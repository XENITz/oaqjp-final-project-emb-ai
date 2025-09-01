from flask import Flask, render_template, request, jsonify
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detection")

@app.route("/emotionDetector")
def sent_emotion():
    text_to_analyze = request.args.get('textToAnalyze')
    response = emotion_detector(text_to_analyze)

    #CREATE THE RETURN STATEMENT
    for i in response:
        answer = f"For the given statement, the system response is\n"
        for emo in response:
            if emo !=  "dominant_emotion":
                answer += f"{emo}: {response[emo]}\n"
            else:
                if response[emo] == "None":
                    answer = "Invalid text! Please try again!."
                else:
                    answer += f"The dominant emotion is: {response[emo]}"
    return answer

@app.route("/")
def render_index_page():
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5003)
