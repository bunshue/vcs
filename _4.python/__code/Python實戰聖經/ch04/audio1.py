from pydub import AudioSegment
from pydub.playback import play

record1 = AudioSegment.from_wav("record1.wav")
play(record1)