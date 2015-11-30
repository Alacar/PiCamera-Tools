import picamera
import time
import os

#Change this to alter the save path
SAVEPATH = 'Videos/'

name = raw_input('Enter a video name: ')
length = input('Enter a video length in seconds: ')
camera = picamera.PiCamera()

#If the directory does not exist, create it
try:
	os.makedirs(SAVEPATH)
except OSError:
	if not os.path.isdir(SAVEPATH):
		raise

print 'Now recording for ' + str(length) + ' seconds.'
camera.start_preview()
camera.start_recording(SAVEPATH + name + '.h264')
time.sleep(length)

camera.stop_preview()
print 'Saving ' + SAVEPATH + name + '.h264'
camera.stop_recording()
