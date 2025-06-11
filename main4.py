import time
import datetime
from pygame import mixer

def logfile(file,stopper):
    with open(file,'a') as f:
        f.write(stopper+'  -  '+str(datetime.datetime.now())+'\n')
        print('Data Successfully Recorded')
def musicplayer(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play(-1)
    while True:
        a= input(f"Type {stopper} to stop :-  ")
        if (a==stopper):
            mixer.music.stop()
            logfile(file+'.txt',stopper)
            break
water=time.time()
eyes=time.time()
physical=time.time()
while True:
    if (time.time()-water>3600):
        musicplayer('water.mp3','drank')
        water=time.time()
    if (time.time()-eyes>1800):
        musicplayer('eyes.mp3','stop')
        eyes=time.time()
    if (time.time()-physical>45*60):
        musicplayer('physical.mp3','pstop')
        physical=time.time()