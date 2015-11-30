import picamera
import time
import os


name = raw_input('What would you like to name the pictures: ')
width = input('Enter a width: ')
height = input('Ener a height: ')
fpm = input('How many frames do you want in a minute: ')
duration = input('How many minutes do you want to record for: ')

camera = picamera.PiCamera()
camera.resolution = (width, height)

savepath = '/media/usb0/' + name

try:
	os.makedirs(savepath)
except OSError:
	if not os.path.isdir(savepath):
		raise

totalframes = fpm*duration
framecount = 0

while framecount < totalframes:
	framecount += 1
	camera.capture(savepath + '/' + name + str(framecount) + '.jpg')
	percent = framecount/totalframes
	print('Image ' + name + str(framecount) + '.jpg has been saved to usb0.               ' + str(framecount) +
		  '/' + str(totalframes) )
	time.sleep(60.0/fpm)
	

