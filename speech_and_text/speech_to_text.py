import speech_recognition as sr
# obtain audio from the microphone
r = sr.Recognizer()
with sr.Microphone() as source:
    print ('Attention! Say something')
    audio = r.listen(source)

# recognize speech using Google Speech Recognition
try:
# for testing purposes, we're just using the default API key
# to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
# instead of `r.recognize_google(audio)`
    data = 'something'
    data = r.recognize_google(audio,language='IT')

except sr.UnknownValueError:
    print ('Attention! Google could not understand audio')
    data='Could not understand anything'
except sr.RequestError as e:

   print ('Attention ! Could not request results from Google service.')

print(data)