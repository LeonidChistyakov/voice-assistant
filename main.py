import speech_recognition as sr
import pyttsx3

import data.commands as cmd
from data.keywords import keywords_en
from data.assistant import VoiceAssistant


def recognize_speech():
    recognized_data = None
    with microphone:
        recognizer.adjust_for_ambient_noise(microphone, duration=2)


        try:
            print("I'm listening")
            assistant.play_voice_assistant_speech("I'm listening")
            audio = recognizer.listen(microphone, 5)

        except sr.WaitTimeoutError:
            return
        
        try:
            print("Started recognition")
            recognized_data = recognizer.recognize_google(audio, language="en-us").lower()

        except:
            pass
        
        return recognized_data


def execute_command(input):
    for word in input:
        for key in keywords_en:
            if word in key:
                return keywords_en[key]()
            else:
                pass
    response = "Command not found..."
    print(response)
    return response


if __name__ == "__main__":

    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Initialize Voice assistant
    assistant = VoiceAssistant()

    # Start speech recognition and response
    voice_input = recognize_speech()
    if voice_input is None:
        response = cmd.recognition_fail()
    else:
        print(voice_input)
        voice_input = voice_input.split(" ")
        response = execute_command(voice_input)
    assistant.play_voice_assistant_speech(response)

