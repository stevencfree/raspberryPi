from time import sleep
import RPi.GPIO as GPIO #gives us access to the GPIO pins
GPIO.setmode(GPIO.BCM)  #sets the pin numbering system we want to use

LED = 17                #pin number driving the LED
delay = 1               #change this number to adjust the frequency at which the light blinks
GPIO.setup(LED,GPIO.OUT)

while True:
    GPIO.output(LED,True)  #turn LED on
    sleep(delay)

    GPIO.output(LED,False) #turn LED off
    sleep(delay)