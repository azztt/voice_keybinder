import speech_recognition as sr

class NoComException(Exception): pass

def get_voice_command(r, m):
    '''
    Input -- nothing\n
    Ouput -- recognize text from speech
    '''
    with m as source:
        audio = r.listen(source, phrase_time_limit=1.5)
    
    text = ''

    try:
        text = r.recognize_google(audio)
    except NoComException as e:
        raise
        # text = ''
        # print("Either nothing was spoken or some unexpected error occurred. Please try again !")

    return text