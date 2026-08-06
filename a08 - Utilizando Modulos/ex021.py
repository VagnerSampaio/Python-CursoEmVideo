import vlc
import time

playsound = vlc.MediaPlayer("synclabmusic-rock-soft-397111.mp3")
playsound.start()

time.sleep(10)
playsound.stop()