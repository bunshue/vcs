from pygame import mixer
mixer.init()
sound = mixer.Sound("wav/hit.wav")
sound.play()