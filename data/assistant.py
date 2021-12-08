import pyttsx3


class VoiceAssistant:
    def __init__(self) -> None:
        self.tts = pyttsx3.init()
        self.setup_voice()


    def setup_voice(self):
        voices = self.tts.getProperty("voices")
        for voice in voices:
            if "ZIRA" in str(voice.id):
                self.tts.setProperty("voice", voice.id)


    def play_voice_assistant_speech(self, text_to_speech):
        self.tts.say(text_to_speech)
        self.tts.runAndWait()

