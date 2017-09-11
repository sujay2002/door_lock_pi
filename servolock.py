import RPi.GPIO as GPIO
import threading
import time
import sys
import os
class servolock:
	def __init__(self):
		GPIO.setmode(GPIO.BOARD)
		self.time_stamp = time.time()
		GPIO.setup(11, GPIO.IN)
		GPIO.setup(13, GPIO.IN)
		GPIO.add_event_detect(11, GPIO.RISING, callback=self.lock)
		GPIO.add_event_detect(13, GPIO.RISING, callback=self.unlock)
	def lock(self,channel):
        	self.time_now = time.time()
		if(self.time_now - self.time_stamp) >= 0.3:	
			print "The Button for Lock is Pressed!\n"
			os.system("python door_lock.py L")
		self.time_stamp = self.time_now
	def unlock(self,channel):
		self.time_now = time.time()
		if(self.time_now - self.time_stamp) >= 0.3:
			print "The Button for Unlock is Pressed!\n"
			os.system("python door_lock.py U")
		self.time_stamp = self.time_now
	def lockit(self):
		print "The Door is Locked!\n"
		os.system("python door_lock.py L")
	def unlockit(self):
		print "Entering from App or Reader:The Door is Unlocked!\n"
		os.system("python door_lock.py U")


