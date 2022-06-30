from gtts import gTTS
import speech_recognition as sr


text_to_say = "è ooooooòlio porca puzzola"
language = "it"

gtts_object = gTTS(text = text_to_say,
                   lang = language,
                   slow = False)

pathmp3 = "content/gtts.mp3"
pathwav = "content/gtts.wav"
gtts_object.save(pathmp3)

from playsound import playsound
  
# for playing note.wav file
playsound(pathmp3)

"""
from pydub import AudioSegment
sound = AudioSegment.from_mp3(pathmp3)
sound.export(pathwav, format="wav")

from IPython.display import Audio

Audio("/content/gtts.wav", autoplay=True)
"""