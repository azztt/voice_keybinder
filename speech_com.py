import speech_recognition as sr
import os

r = sr.Recognizer()
m = sr.Microphone()

# print("say now in 5 seconds")
with m as source:
    audio = r.listen(source, timeout=2000)

HOUNDIFY_CLIENT_ID = str(os.getenv('HOUNDIFY_CLIENT_ID'))
HOUNDIFY_CLIENT_KEY = str(os.getenv('HOUNDIFY_CLIENT_KEY'))
# text="jyhjhv"
text = r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY)
print("you probably said: " + text)
# try:
#     print("Houndify thinks you said " + r.recognize_houndify(audio, client_id=HOUNDIFY_CLIENT_ID, client_key=HOUNDIFY_CLIENT_KEY))
# except sr.UnknownValueError:
#     print("Houndify could not understand audio")
# except sr.RequestError as e:
#     print("Could not request results from Houndify service; {0}".format(e))

