#import modules
import pandas as pd
import numpy as np
import speech_recognition as sr


pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns', 300)


r = sr.Recognizer()

with sr.Microphone() as source:
    print('Talk into Microphone')
    audio = r.listen(source)

    try:
        text = recognize_google(audio)
        print('You said : {}'.format(text))
    except:
        print('Cannot recognise your voice')
