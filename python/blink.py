from time import sleep
import RPi.GPIO as GPIO #gives us access to the GPIO pins
GPIO.setmode(GPIO.BCM)  #sets the pin numbering system we want to use

LED = 21
GPIO.setup(LED,GPIO.OUT)

while True:
    GPIO.output(LED,True)
    sleep(1)

    GPIO.output(LED,False)
    sleep(1)