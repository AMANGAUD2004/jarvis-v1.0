# pip install SpeechRecognition 
# pip install mtranslate
# pip install colorama
# pip install pyaudio
import speech_recognition as sr
import os
import threading



from mtranslate import translate


from colorama import Fore,Back,Style,init

init(autoreset=True)

from colorama import Fore, Style, init



def print_loop():
    while True:
        print(Fore.GREEN + "Listening...", end="", flush=True)
        print(Style.RESET_ALL, end="", flush=True)

def translate_hindi_to_english(text):
    english_text = translate(text,"en-us")
    return english_text

def Speech_to_Text_python():
    Recognizer = sr.Recognizer()
    Recognizer.energy_threshold = 4000
    Recognizer.dynamic_energy_threshold = False
    Recognizer.dynamic_energy_adjustment_damping = 0.15
    Recognizer.dynamic_energy_ratio = 1.5
    Recognizer.pause_threshold = 0.8
    Recognizer.operation_timeout = None
    Recognizer.pause_threshold = 0.8    
    Recognizer.non_speaking_duration = 0.8

    with sr.Microphone() as source:
        Recognizer.adjust_for_ambient_noise(source)
        while True:
            print(Fore.GREEN + "Listening...", end="", flush=True)
        
            try:
                audio = Recognizer.listen(source, timeout=None)
                print("\r" + Fore.LIGHTBLACK_EX + "Recog...", end="", flush=True)
                Recognizer_text = Recognizer.recognize_google(audio).lower()
                if Recognizer_text:
                    translated_text = translate_hindi_to_english(Recognizer_text)
                    print("\n" + Fore.BLUE + "NethyTech: " + translated_text)
                    return translated_text
                else:
                    return ""
            except sr.UnknownValueError:
                Recognizer_text = ""
            finally:
                print("\r", end="", flush=True)

            os.system('cls' if os.name == 'nt' else 'clear')

        stt_thread = threading.Thread(target=specch_to_Text_python)
        print_thread = threading.Thread(target=print_loop)
        stt_thread.start()
        print_loop.start()
        stt_thread.join()
        print_loop.join()
        

Speech_to_Text_python()

