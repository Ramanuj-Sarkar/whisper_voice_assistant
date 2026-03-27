from gtts import gTTS
from pygame import mixer
import tempfile, os

mixer.init()

def speak(text: str):
    tmp = tempfile.mktemp(suffix=".mp3")
    gTTS(text=text, lang="en").save(tmp)
    mixer.music.load(tmp)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    mixer.music.unload()
    os.remove(tmp)
