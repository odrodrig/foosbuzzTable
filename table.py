import RPi.GPIO as GPIO
import signal
import sys
import time
import ibmiotf.device

inputPin = 40
inputPin2 = 32
buttonPin = 18

org = ""
type = ""
id = ""
method="token"
token=""

GPIO.setmode(GPIO.BOARD)
GPIO.setup(inputPin,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(inputPin2,GPIO.IN,pull_up_down=GPIO.PUD_UP)
GPIO.setup(buttonPin,GPIO.IN)

def signal_handler(signal, frame):
	print '\n Exiting'
	GPIO.cleanup()
	table.disconnect()
	sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)

def sensor_callback(gpio_id):
	data=1
	print "goal Team 1"
	table.publishEvent("status", "json", data)
	time.sleep(1)

def sensor2_callback(gpio_id):
	data=2
	print "goal Team 2"
	table.publishEvent("status", "json", data)
	time.sleep(1)

def button_callback(gpio_id):
	data=0
	print "Game Reset"
	table.publishEvent("status", "json", data)

try:

	options= {
		"org":org,
		"type":type,
		"id":id,
		"auth-method":method,
		"auth-token":token
	}
	
	table = ibmiotf.device.Client(options)
	table.connect()

	GPIO.add_event_detect(inputPin, GPIO.FALLING, callback=sensor_callback, bouncetime=1000)
	GPIO.add_event_detect(buttonPin, GPIO.FALLING, callback=button_callback, bouncetime=1000)
	GPIO.add_event_detect(inputPin2, GPIO.FALLING, callback=sensor2_callback, bouncetime=1000)



	while True:
		time.sleep(1)

except (KeyboardInterrupt, SystemExit):
	raise

except ibmiotf.ConnectionException as e:
	print e
