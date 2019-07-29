from pydub import AudioSegment
from pydub.playback import play
from MorseList import alphanumeric_all
import os
import time

data = input('Input data: ')
output = [] 
letters = list(data.upper())
for letter in letters:
    if letter in alphanumeric_all:
        letter, audio = alphanumeric_all.get(letter)
        output.append(letter)
        if os.path.exists(os.path.dirname(audio)):
            snd = AudioSegment.from_ogg(audio)
            play(snd)
        else:
            time.sleep(0.3)
    else:
        output.append('/')
print(''.join(output))


