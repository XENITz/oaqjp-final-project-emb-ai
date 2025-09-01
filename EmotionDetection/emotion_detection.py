import requests
import json

def emotion_detector(text_to_analyze):
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(api_url, json=data, headers=header )

    #HANDLE ERROR
    print("THIS IS ERROR CODE: ", response.status_code)
    error_code = response.status_code

    #DOMINANT EMOTION
    result = response.json()
    dominant_emotion = ""
    number = 0
    emotions = {}
    if error_code == 200:
        results = result["emotionPredictions"][0]
        for emotion in results["emotion"]:
            value = results["emotion"][emotion]
            emotions[emotion] = value
            if value > number:
                number = value
                dominant_emotion = emotion
        emotions["dominant_emotion"] = dominant_emotion
    elif error_code == 400:
        emotions = {"anger": "None",
                    "disgust": "None",
                    "fear": "None",
                    "joy": "None",
                    "sadness": "None",
                    "dominant_emotion": "None"}

    return emotions
