import RPi.GPIO as gpio

from time import sleep
dac=[8,11,7,1,0,5,12,6]
gpio.setmode(gpio.BCM)
gpio.setup(2, gpio.OUT)
gpio.setup(dac, gpio.OUT, initial=gpio.HIGH)
pwm=gpio.PWM(2,1000)
pwm.start(0)
try:
    while(True):
        DutyCicle=int(input())
        pwm.ChangeDutyCycle(DutyCycle)
        print("{:.2f}".format(DutyCicle*3.3/100))
finally:
    gpio.output(2,0)
    gpio.output(dac,0)
    gpio.cleanup()