from time import sleep
import RPi.GPIO as GPIO #gives us access to the GPIO pins
GPIO.setmode(GPIO.BCM)  #sets the pin numbering system we want to use

green = 17  #set variables for the pin numbers driving each LED
yellow = 27
red = 22

GPIO.setup(green, GPIO.OUT)  #configure GPIO pins to output mode
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

while True:
    GPIO.output(red, False)  #turn on green light for 2 seconds
    GPIO.output(green, True)
    sleep(2)

    GPIO.output(green, False) #turn on yellow light for 1 second
    GPIO.output(yellow, True)
    sleep(1)

    GPIO.output(yellow, False) #turn on red light for 3 seconds
    GPIO.output(red, True)
    sleep(3)