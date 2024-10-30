import logging
import queue
import pyttsx3
import speech_recognition as sr
from typing import Dict

class VoiceManager:
    """Handles voice input/output"""
    def __init__(self, config: Dict):
        self.config = config
        self.tts_engine = None
        self.stt_engine = None
        self.voice_queue = queue.Queue()

    async def initialize(self):
        """Initialize voice systems"""
        try:
            # Initialize TTS engine
            self.tts_engine = pyttsx3.init()
            self.tts_engine.setProperty('voice', self.config["voice"]["voice_id"])
            self.tts_engine.setProperty('rate', self.config["voice"]["speaking_rate"])
            self.tts_engine.setProperty('pitch', self.config["voice"]["pitch"])

            # Initialize STT engine
            self.stt_engine = sr.Recognizer()

        except Exception as e:
            logging.error(f"Failed to initialize voice manager: {str(e)}")

    async def speak(self, text: str):
        """Convert text to speech"""
        try:
            self.tts_engine.say(text)
            self.tts_engine.runAndWait()
        except Exception as e:
            logging.error(f"Failed to speak text: {str(e)}")

    async def listen(self) -> str:
        """Convert speech to text"""
        try:
            with sr.Microphone() as source:
                self.stt_engine.adjust_for_ambient_noise(source)
                audio = self.stt_engine.listen(source)
                return self.stt_engine.recognize_google(audio)
        except sr.UnknownValueError:
            logging.error("Speech recognition could not understand audio")
        except sr.RequestError as e:
            logging.error(f"Could not request results from speech recognition service: {e}")
        return ""
