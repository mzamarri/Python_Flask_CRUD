"""
This module uses Watsons NLP AI libraries to analyze a piece of text using the sentiment_analyzer 
function
"""
import json
import requests

def sentiment_analyzer(text_to_analyze):
    """
    This function takes some text and analyzes it using the Watson NLP AI library. It returns
    a dictionary with a label and score value
    """
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = {"raw_document": {"text": text_to_analyze}}
    response = requests.post(url, json = myobj, headers=header)
    formatted_response = json.loads(response.text)
    print(response.status_code)
    if response.status_code == 200:
        label = formatted_response['documentSentiment']['label']
        score = formatted_response['documentSentiment']['score']
    elif response.status_code == 500:      
        label = None
        score = None
    return {'label': label, 'score': score}
    
