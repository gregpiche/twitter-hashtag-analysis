import json
import os
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions

def analyze(text):
    authenticator = IAMAuthenticator(os.getenv('IBM_WATSON_NLU_KEY'))
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        version='2022-04-07',
        authenticator=authenticator
    )

    natural_language_understanding.set_service_url(os.getenv('IBM_WATSON_NLU_URL'))


    response = natural_language_understanding.analyze(
        html=text,
        features=Features(emotion=EmotionOptions(document=True))).get_result()
    
    return response
