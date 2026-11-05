"""Emotion detection using the Watson NLP EmotionPredict function."""
import json

import requests

URL = (
    "https://sn-watson-emotion.labs.skills.network/v1/"
    "watson.runtime.nlp.v1/NlpService/EmotionPredict"
)
HEADERS = {"grpc-metadata-mm-model-id": "emotion_aggregated-workflow_lang_en_stock"}
REQUEST_TIMEOUT_SECONDS = 30


def emotion_detector(text_to_analyze):
    """Return the emotion scores for the text along with the dominant emotion."""
    input_json = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(
        URL, json=input_json, headers=HEADERS, timeout=REQUEST_TIMEOUT_SECONDS
    )

    formatted_response = json.loads(response.text)
    emotions = formatted_response["emotionPredictions"][0]["emotion"]
    scores = {
        "anger": emotions["anger"],
        "disgust": emotions["disgust"],
        "fear": emotions["fear"],
        "joy": emotions["joy"],
        "sadness": emotions["sadness"],
    }
    dominant_emotion = max(scores, key=scores.get)

    return {**scores, "dominant_emotion": dominant_emotion}
