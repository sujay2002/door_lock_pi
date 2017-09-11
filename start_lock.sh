screen -m -d -S for_lock
screen -S for_lock -X stuff "sudo python /home/pi/locker.py & $(echo '\r')"
