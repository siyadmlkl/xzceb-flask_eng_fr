import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
import os
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url=os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(version='2018-05-01',authenticator=authenticator)
language_translator.set_service_url(url)

#Translate from English to French
def english_to_french(english_text):
    french_text = language_translator.translate(text=english_text,model_id = 'en-fr').result['translations'][0]['translation']
    return french_text

#Translate from French to English
def french_to_english(french_text):
    english_text= language_translator.translate(text=french_text,model_id = 'fr-en').result['translations'][0]['translation']
    return english_text

print(english_to_french("i want to learn"))