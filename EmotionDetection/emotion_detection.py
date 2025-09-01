import requests
import json

def emotion_detector(text_to_analyze):
    api_url = 'https://sn-watson-emotion.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/EmotionPredict'
    header = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
    data = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(api_url, json=data, headers=header )
    result = response.json()
    results = result["emotionPredictions"][0]

    #DOMINANT EMOTION
    dominant_emotion = ""
    number = 0
    emotions = {}
    for emotion in results["emotion"]:
        value = results["emotion"][emotion]
        emotions[emotion] = value
        if value > number:
            number = value
            dominant_emotion = emotion
    emotions["dominant_emotion"] = dominant_emotion    

    return emotions