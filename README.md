# door_lock_pi
#Author of the code is : Sujay Kanungo
For any Bugs Please contact author on Email : sujay2002@gmail.com
# The Functionality of the Implementation is below:

1. Able to Read RFID cards for Authentication and will open and Close the Door
2. Able to Read Button inputs for Opening and Closing the Door
3. Has a REST API interface available to be able to close and open the Door.
4. REST API endpoint uses Basic HTTP Authentication Mechanism with a Valid Username and Password

Steps to Install the Application:

a.Dependency : flask,flask_httpauth and pirc522

b.Clone the code from git and copy all the files in your raspberry pi under /home/pi

c.Give Executable Access to locker.py

d.copy the file lock under /etc/init.d and go the folder /etc/init.d

e.Execute the command "update-rc.d lock defaults"

f.use the command line "python door_lock.py L" to Move the Servo to Lock Position for the first time For installation

Start the program under /home/pi as python locker.py
Scan the RFID key fobs and Edit the key data in card_data.json, Whenever you scan a new key Fob it will print some card data such as [82,101,194,16,220] copy that from the output screen and update the card_data.json dictionary value or add a new value as you see fit.
Reboot the Pi and the software will start working.

The Layout of the Pi and Circuit can be found on the Below Mentioned Link:

