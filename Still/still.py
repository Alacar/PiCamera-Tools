import picamera
import time


width = input('Enter the image width: ')
height = input('Enter the image height: ')
name = raw_input('Enter a file name: ')

with picamera.PiCamera() as camera:
	camera.resolution = (width, height)
	camera.start_preview()
	time.sleep(5)
	camera.capture( name + '.jpg')
