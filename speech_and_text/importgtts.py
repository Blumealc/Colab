from gtts import gTTS


text_to_say = "è ooooooòlio porca puzzola"
language = "it"

gtts_object = gTTS(text = text_to_say,
                   lang = language,
                   slow = False)

gtts_object.save("content/gtts.wav")

from playsound import playsound
  
# for playing note.wav file
playsound('content/gtts.wav')

"""
from IPython.display import Audio

Audio("/content/gtts.wav", autoplay=True)
"""