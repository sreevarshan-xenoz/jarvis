import logging
from config_manager import ConfigManager
from voice_biometrics import VoiceBiometrics
from secure_storage import SecureStorage
from encryption_manager import EncryptionManager  # Make sure you import this
from emotion_recognition import EmotionRecognition
from multiple_models import MultipleAIModels

class JarvisCore:
    def __init__(self):
        self.config_manager = ConfigManager()
        self.voice_biometrics = VoiceBiometrics()
        self.encryption_manager = EncryptionManager()  # Create an instance of EncryptionManager
        self.secure_storage = SecureStorage(self.encryption_manager)  # Pass it to SecureStorage
        self.emotion_recognition = EmotionRecognition()
        self.ai_models = MultipleAIModels()

        # Example data for demonstration
        self.user_data = {'username': 'test_user', 'data': 'Sensitive data'}

    def authenticate_user(self, username):
        # Simulate user authentication
        if self.voice_biometrics.authenticate(username):
            logging.info(f"User {username} authenticated successfully.")
            return self.user_data['data']
        else:
            logging.error(f"User {username} authentication failed.")
            return None

    def run(self):
        logging.info("Starting Jarvis...")
        user_data = self.authenticate_user('test_user')
        if user_data:
            logging.info(f"Retrieved data: {user_data}")

            # Generate response using DialoGPT
            user_input = "Hello, how can I help you today?"
            response_dialogpt = self.ai_models.generate_response(user_input, model_number=1)
            logging.info(f"DialogGPT Response: {response_dialogpt}")

            # Generate response using the second model
            response_other = self.ai_models.generate_response(user_input, model_number=2)
            logging.info(f"Other Model Response: {response_other}")

            # Simulate emotion recognition
            detected_emotion = self.emotion_recognition.analyze_text("I'm so happy!")
            logging.info(f"Detected Emotion: {detected_emotion}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    jarvis = JarvisCore()
    jarvis.run()
