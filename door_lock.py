import RPi.GPIO as GPIO
import time
import sys

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)

p = GPIO.PWM(16, 50)
p.start(0)

if (str(sys.argv[1]) == "L"):
	print "The Door is Locked!\n"
	p.ChangeDutyCycle(2.5)  # turn towards 0 degree
	time.sleep(1) # sleep 1 second
elif(str(sys.argv[1]) == "U"):
	print "The Door is Unlocked!\n"
	p.ChangeDutyCycle(12.5) # turn towards 180 degree
      	time.sleep(1) # sleep 1 second
p.stop()
GPIO.cleanup()
