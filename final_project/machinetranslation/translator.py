""" author: alitarika - Tarik // python for translation en fr"""

import json
import os
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']
authenticator = IAMAuthenticator('hnJqp9G_lOhKcFYqi7uCxyVBfvFZ4AR96JNy_TkEJLc8')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.eu-de.language-translator.watson.cloud.ibm.com/instances/f0e2de91-e3d6-43ab-af05-6c56ce39a138')

def englishtofrench(englishtext):
    """ translate func english to french """
    frenchtext = language_translator.translate(text=englishtext, model_id='en-fr').get_result().get("translations")[0].get("translation")
    return frenchtext

def frenchtoenglish(frenchtext):
    """ translate func french to english """
    englishtext = language_translator.translate(text=frenchtext, model_id='fr-en').get_result().get("translations")[0].get("translation")
    return englishtext