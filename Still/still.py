#!/usr/bin/python

import picamera
import time
import os

#Change this if you want to save the image to a new location
SAVEPATH = 'Photos/'

width = input('Enter the image width: ')
height = input('Enter the image height: ')
name = raw_input('Enter a file name: ')

with picamera.PiCamera() as camera:
	camera.resolution = (width, height)
	camera.start_preview()
	print 'Taking picture in'
	for i in range(0, 5):
		print(str(5 - i) + '...')
		time.sleep(1)
	print 'Now saving the picture to ' + SAVEPATH + name + '.jpg'
	
	#If the directory does not exist, create it
	try:
		os.makedirs(SAVEPATH)
	except OSError:
		if not os.path.isdir(SAVEPATH):
			raise
 
	camera.capture( SAVEPATH + name + '.jpg')
