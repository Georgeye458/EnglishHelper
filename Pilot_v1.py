#import modules
import pandas as pd
import numpy as np
import speech_recognition as sr


pd.set_option('display.max_rows', 15)
pd.set_option('display.max_columns', 300)


r = sr.Recognizer()

# This is an implementation with the mircrophone. Let's try one without.
# with sr.Microphone() as source:
#     print('Talk into Microphone')
#     audio = r.listen(source)

#     try:
#         text = recognize_google(audio) #Can use recognize_sphinx() if you want offline.
#         print('You said : {}'.format(text))
#     except:
#         print('Cannot recognise your voice')

stocks_audio = sr.AudioFile('stocks.wav')

with stocks_audio as source:
    audio = r.record(source, duration=10)

text = r.recognize_google(audio)
print(text)
