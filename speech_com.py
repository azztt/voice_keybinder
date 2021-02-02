import speech_recognition as sr

def get_voice_command(r, m):
    '''
    Input -- nothing
    Ouput -- recognize text from speech
    '''
    # r = sr.Recognizer()
    # m = sr.Microphone()

    # r.energy_threshold = threshold
    with m as source:
        audio = r.listen(source, phrase_time_limit=1)
    
    text = ''

    try:
        text = r.recognize_google(audio)
    except Exception as e:
        text = ''
        print(e)
        print("Either nothing was spoken or some unexpected error occurred. Please try again !")

    return text