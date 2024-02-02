from dotenv import load_dotenv
from datetime import datetime
import os

# Import namespaces
import azure.cognitiveservices.speech as speech_sdk
from playsound import playsound

def main():    
    try:        
        global speech_config        
        global translation_config        
        
        # Get Configuration Settings        
        load_dotenv()        
        ai_key = os.getenv('SPEECH_KEY')        
        ai_region = os.getenv('SPEECH_REGION')        
        
        # Configure translation        
        translation_config = speech_sdk.translation.SpeechTranslationConfig(ai_key, ai_region)        
        translation_config.speech_recognition_language = 'en-US'        
        translation_config.add_target_language('fr')        
        translation_config.add_target_language('es')        
        translation_config.add_target_language('hi')        
        print('Ready to translate from',translation_config.speech_recognition_language)        
        
        # Configure speech        
        speech_config = speech_sdk.SpeechConfig(ai_key, ai_region)        
        
        # Get user input        
        targetLanguage = ''        
        while targetLanguage != 'quit':            
            targetLanguage = input('\nEnter a target language\n fr = French\n es = Spanish\n hi = Hindi\n Enter anything else to stop\n').lower()            
            if targetLanguage in translation_config.target_languages:                
                Translate(targetLanguage)            
            else:                
                targetLanguage = 'quit'                    
    except Exception as ex:        
        print(ex)def Translate(targetLanguage):    
        translation = ''    
        
        # Translate speech    
        audio_config = speech_sdk.AudioConfig(use_default_microphone=True)    
        translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config)    
        print("Speak now...")    
        result = translator.recognize_once_async().get()    
        print('Translating "{}"'.format(result.text))    
        translation = result.translations[targetLanguage]    
        print(translation)    
        
        # Synthesize translation    
        audioFile = 'station.wav'    
        playsound(audioFile)    
        audio_config = speech_sdk.AudioConfig(filename=audioFile)    
        translator = speech_sdk.translation.TranslationRecognizer(translation_config, audio_config = audio_config)    
        print("Getting speech from file...")    
        result = translator.recognize_once_async().get()    
        print('Translating "{}"'.format(result.text))    
        translation = result.translations[targetLanguage]    
        print(translation)
        
if __name__ == "__main__":    main()