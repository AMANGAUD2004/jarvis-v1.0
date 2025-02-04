import os
import subprocess
import tempfile
# pip install playsound==1.2.2
from playsound import playsound
import threading

def speak(text: str, voice: str = 'en-CA-LiamNeural') -> None:
    try:
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as temp:
            output_file = temp.name

        command = f'edge-tts --voice {voice} --text "{text}" --write-media "{output_file}"'
        
        subprocess.run(command, shell=True, check=True)

        # Fixed args name
        threading.Thread(target=playsound, args=(output_file,)).start()
    except Exception as e:
        print("Error:", e)


while True:
    x = input("")
    if x.lower() == "exit":
        break 
    speak(x)  
