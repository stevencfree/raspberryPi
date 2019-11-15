from time import sleep
import RPi.GPIO as GPIO #gives us access to the GPIO pins
GPIO.setmode(GPIO.BCM)  #sets the pin numbering system we want to use

button = 25  #set variable for the pin number used

GPIO.setup(button, GPIO.IN)  #configure GPIO pin to input mode

while True:
    if GPIO.input(button):
        print("Button pressed")
    else:
        print("Button not pressed")
    sleep(0.1)