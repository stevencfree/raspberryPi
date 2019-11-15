import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

green = 17
yellow = 27
red = 22

GPIO.setup(green, GPIO.OUT)
GPIO.setup(yellow, GPIO.OUT)
GPIO.setup(red, GPIO.OUT)

while true
    GPIO.output(red, False)
    GPIO.output(green, True)
    time.sleep(2)

    GPIO.output(green, False)
    GPIO.output(yellow, True)
    time.sleep(1)

    GPIO.output(yellow, False)
    GPIO.output(red, True)
    time.sleep(3)