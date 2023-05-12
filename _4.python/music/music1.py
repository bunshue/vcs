from pygame import mixer

filename1 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/02 渡り鳥仁義(1984.07.01-候鳥仁義).mp3'
filename2 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/16.監獄風雲.mp3'
filename3 = 'C:/_git/vcs/_1.data/______test_files1/_wav/harumi99.wav'

'''
mixer.init()
mixer.music.load(filename1)
mixer.music.play()
'''

'''
from pygame import mixer

filename4 = 'C:/_git/vcs/_1.data/______test_files1/_mp3/mario.mp3'

mixer.init()
mixer.music.load(filename4)
mixer.music.play()
'''

from pygame import mixer

mixer.init()
sound = mixer.Sound(filename3)
sound.play()

