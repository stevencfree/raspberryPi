from time import sleep
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

LED = 17
button = 25
GPIO.setup(LED, GPIO.OUT)
GPIO.setup(button, GPIO.IN)

toggle = False
while True:
	GPIO.output(LED, toggle)
	
	if GPIO.input(button):
		toggle = not toggle
		print("Button pressed")
		while GPIO.input(button):	
			pass

