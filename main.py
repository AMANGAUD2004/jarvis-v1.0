import pygame
import random
import asyncio
import edge_tts
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

async def TextToAudioFile(text: str) -> None:
    """Converts text to an audio file."""
    file_path = 'data.mp3'
    if os.path.exists(file_path):
        os.remove(file_path)
    
    voice = os.getenv('AssistantVoice', 'en-US-JennyNeural')  # Default voice
    communicate = edge_tts.Communicate(text, voice, pitch='+5Hz', rate='+22%')
    await communicate.save(file_path)

def TextToSpeech(text: str, func=lambda r=None: True) -> None:
    """Plays the converted text audio file."""
    try:
        # Ensure an event loop is available
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        loop.run_until_complete(TextToAudioFile(text))
        
        # Initialize pygame mixer
        try:
            pygame.mixer.init()
        except pygame.error as e:
            print(f"Pygame mixer initialization failed: {e}")
            return

        pygame.mixer.music.load('data.mp3')
        pygame.mixer.music.play()
        
        while pygame.mixer.music.get_busy():
            if not func():
                break
            pygame.time.Clock().tick(10)
    except Exception as e:
        print(f"Error in TextToSpeech: {e}")
    finally:
        pygame.mixer.music.stop()
        pygame.mixer.quit()

def TTS(text: str, func=lambda r=None: True) -> None:
    """Handles TTS for long texts by splitting and adding additional instructions."""
    responses = [
        'The rest of the result has been printed to the chat screen, kindly check it out.',
        'You can see the rest of the text on the chat screen.',
        'The remaining part of the text is now on the chat screen.',
        "You'll find more text on the chat screen.",
        'Please check the chat screen for additional text.'
    ]
    
    data = text.split('.')
    if len(data) > 4 and len(text) >= 250:
        prompt = ' '.join(data[:2]) + '. ' + random.choice(responses)
        TextToSpeech(prompt, func)
    else:
        TextToSpeech(text, func)

if __name__ == '__main__':
    while True:
        user_input = input('Enter the text: ')
        if user_input.lower() == 'exit':
            break
        TTS(user_input)
