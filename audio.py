import speech_recognition
from playsound import playsound
from gtts import gTTS

def say_string(string):
    tts = gTTS(string, lang='pt')
    tts.save('system_audio.mp3')
    playsound('system_audio.mp3')

def listen_microphone(message=None):
    # Creates a mic instance
    microfone = speech_recognition.Recognizer()
    #listen to mic
    with speech_recognition.Microphone() as source:
        # Reduces ambient noises
        microfone.adjust_for_ambient_noise(source)

        if message:
            say_string(message)
        # Audio capture
        audio = microfone.listen(source, timeout=3)

        try:
            result = microfone.recognize_google(audio, language='PT-BR')
            return result
        except speech_recognition.UnknownValueError:
            return None
