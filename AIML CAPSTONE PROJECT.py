import warnings
warnings.filterwarnings("ignore", category=UserWarning)
import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time

# --- CO2: Verified Language Database ---
SUPPORTED_LANGUAGES = {
    "hindi": "hi", "marathi": "mr", "bengali": "bn", "tamil": "ta",
    "telugu": "te", "kannada": "kn", "malayalam": "ml", "gujarati": "gu",
    "french": "fr", "japanese": "ja", "spanish": "es", "german": "de",
    "korean": "ko", "english": "en"
}

def listen_to_user(prompt):
    recognizer = sr.Recognizer()
    recognizer.dynamic_energy_threshold = True 
    
    with sr.Microphone() as source:
        print(f"\n[SYSTEM]: {prompt}")
        recognizer.adjust_for_ambient_noise(source, duration=1.2)
        print("Listening...")
        try:
            audio = recognizer.listen(source, timeout=5, phrase_time_limit=10)
            return recognizer.recognize_google(audio).lower()
        except:
            return None

def voice_translator():
    
    sentence = listen_to_user("Please speak your sentence.")
    if not sentence:
        return 

    print(f"Captured: {sentence}")


    spoken_lang = listen_to_user("Which language should I translate this to?")
    if not spoken_lang:
        return 
    
    
    target_code = None
    for lang_name, code in SUPPORTED_LANGUAGES.items():
        if lang_name in spoken_lang:
            target_code = code
            break

    if target_code:
        try:
            
            translated_text = GoogleTranslator(source='auto', target=target_code).translate(sentence)
            print(f"Translated: {translated_text}")

            
            tts = gTTS(text=translated_text, lang=target_code)
            filename = "temp_voice.mp3"
            tts.save(filename)

            pygame.mixer.init()
            pygame.mixer.music.load(filename)
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                time.sleep(0.1)
            
            
            pygame.mixer.music.unload()
            if os.path.exists(filename):
                os.remove(filename)
                
        except Exception:
            pass
    else:
        print(f"[SYSTEM]: Language not supported.")

if __name__ == "__main__":
    voice_translator()