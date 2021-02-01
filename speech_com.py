import speech_recognition as sr

def get_voice_command():

    r = sr.Recognizer()
    m = sr.Microphone()

    with m as source:
        audio = r.listen(source, phrase_time_limit=1)

    text = r.recognize_google(audio)
    return text