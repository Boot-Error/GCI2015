#!/usr/bin/env python

import time
import picamera

# setting up camera hardware
with picamera.PiCamera() as cam:
	
	# loop to capture images 10 times
	for count in range(10):
		
		print "[+] Capturing Image, count %d" % count
		cam.capture("image%d.jpg" % count)
		# minimum 
		time.sleep(2)

print "[*] Done Capturing!"
