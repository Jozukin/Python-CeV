import vlc
from time import sleep
media = vlc.MediaPlayer("F:\\Users\\JV\\Music\\Avenged Sevenfold\\The Stage\\01 - The Stage.mp3")
media.play()
sleep(5)  # Or however long you expect it to take to open vlc
while media.is_playing():
    sleep(1)
