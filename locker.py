import requests
import threading
import time
from flask import Flask,g
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
import sys
sys.path.insert(0, "/home/pi/pi-rc522/ChipReader")

from pirc522 import RFID
from servolock import servolock
import signal
import json
from pprint import pprint
with open('card_data.json') as data_file:
	extract = json.load(data_file)
import time
import os

app = Flask(__name__)
auth = HTTPBasicAuth()
users = {
	"admin":generate_password_hash("password"),
	"guest":generate_password_hash("guest123")
}
srv = servolock()
@app.before_first_request
def activate_job():
    def run_job():
	rdr = RFID()

	util = rdr.util()

	util.debug = False
	door_locked = 1
	while True:

    	#Request tag

    		(error, data) = rdr.request()

    		if not error:

        		print ("\nDetected")



        		(error, uid) = rdr.anticoll()

        		if not error:

            		#Print UID

            			print ("Card read UID: "+str(uid[0])+","+str(uid[1])+","+str(uid[2])+","+str(uid[3])+","+str(uid[4]))
            			print uid
				for i in xrange (len(extract["data"])):
				    for value in extract["data"][i].itervalues():
	    				  if uid == value:
						print "White Card"
						if (door_locked):
							srv.lockit()
							door_locked = 0	
					 	else:
							srv.unlockit()
							door_locked = 1
					
	    		  		  else:
						continue
						print "Tag Not Known!"
				

            			time.sleep(1)
	

    thread = threading.Thread(target=run_job)
    thread.start()

@auth.verify_password
def verify_password(username,password):
	if username in users:
		g.user = None
        	if check_password_hash(users.get(username), password):
			g.user = username
			return True
    	return False

@app.route("/")
@auth.login_required
def hello():
    return "The Door Locker is Ready!!! %s" % g.user 
@app.route("/lockme")
@auth.login_required
def lockme():
    srv.lockit()
    return "The App Has Locked The Door!%s"% g.user
@app.route("/unlockme")
@auth.login_required
def unlockme():
    srv.unlockit() 
    return "The App has Unlocked The Door!%s" % g.user

def start_runner():
    def start_loop():
        not_started = True
        while not_started:
            print('In start loop')
            try:
                r = requests.get('http://admin:password@127.0.0.1:5000/')
                if r.status_code == 200:
                    print('Server started, quiting start_loop')
                    not_started = False
                print(r.status_code)
            except:
                print('Server not yet started')
            time.sleep(2)

    print('Started runner')
    thread = threading.Thread(target=start_loop)
    thread.start()

if __name__ == "__main__":
    start_runner()
    app.run(host='0.0.0.0')
