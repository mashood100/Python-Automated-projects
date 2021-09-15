import speech_recognition as sr
listener = sr.Recognizer()
try:
     with sr.Microphone() as source:
         print('listning...')
         voice = listener.listen(source)
         commad =listener.recognize_google(voice)
         commad = commad.lower()
         if 'alexa' in commad:
             print(commad)
         print(commad)
except:    
    pass