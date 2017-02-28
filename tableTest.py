import RPi.GPIO as GPIO
import signal
import time
import sys

inputPin = 40
inputPin2 = 32
buttonPin = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(inputPin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin,GPIO.IN)

def signal_handler(signal, frame):
	print '\n Exiting'
	GPIO.cleanup()
	sys.exit(0)

def sensor_callback(gpio_id):
	print "Goal Team 1"

def sensor_callback2(gpio_id):
	print "Goal Team 2"

def button_callback(gpio_id):
	print "Reset Button Pushed"

try:
	GPIO.add_event_detect(inputPin, GPIO.FALLING, callback=sensor_callback, bouncetime=1000)
	GPIO.add_event_detect(inputPin2, GPIO.FALLING, callback=sensor_callback2, bouncetime=1000)
	GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=button_callback, bouncetime=1000)

	while True:
		time.sleep(1)

except (KeyboardInterrupt, SystemExit):
	raise
