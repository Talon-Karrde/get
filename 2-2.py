import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
dac=[8,11,7,1,0,5,12,6]
number=[0,0,0,0,0,0,0,0]

GPIO.setup(dac, GPIO.OUT)
for i in range(8):
    GPIO.output(dac[i], number[i])

time.sleep(15)
GPIO.output(dac,0)
GPIO.cleanup()

#255 3,228
#127 1,667
#64 0,865
#32 0,458
#5 0,117
#0 0,053