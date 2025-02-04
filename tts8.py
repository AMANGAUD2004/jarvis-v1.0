import requests
import playsound
import os
from typing import Union

def generate_audio(message: str, voice: str = "Brian") -> Union[None, bytes]:
    url = f"https://api.streamelements.com/kappa/v2/speech?voice={voice}&text={message}"
    
    headers = {'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'}

    try:
        result = requests.get(url=url, headers=headers)
        if result.status_code == 200:
            return result.content 
        else:
            print(f"Error: {result.status_code}")
            return None
    except Exception as e:
        print(f"Error: {e}")
        return None

def speak(message: str, voice: str = "Brian", folder: str = "", extension: str = "mp3") -> Union[None, str]:
    try:
        result_content = generate_audio(message, voice)
        if result_content:
            file_path = os.path.join(folder, f"{voice}.{extension}")
            with open(file_path, "wb") as file:
                file.write(result_content)
            playsound.playsound(file_path)  # Remove the "wb" argument
            os.remove(file_path)  # Clean up by removing the file after playing it
            return None
        else:
            return "Failed to generate audio."
    except Exception as e:
        print(f"An error occurred: {e}")
        return str(e)

# Example usage
speak("Hello sir, I am your assistant may i help you")
