import picamera
import time
import os

SAVEPATH = '/media/usb0/'

#Get user input main loop
confirm = 'y'
while confirm == 'y':
	#Get name of picture set
	name = raw_input('What would you like to name the picture set: ')
	while name == '':
		name = raw_input('Incorrect name. Try again: ')

	#Get width of images
	width = input('Enter the desired image width: ')
	while width < 1:
		width = input('Incorrect width. Try again: ')

	#Get height of images
	height = input('Enter the desired image height: ')
	while height < 1:
		height = input('Incorrect height. Try again: ')

	#Get amount of pictures per minute
	fpm = input('How many pictures do you want in a minute: ')
	while fpm <= 0:
		fpm = input('Incorrect amount of time. Try again: ')

	#Get how long the program should run for in minutes
	duration = input('How many minutes do you want to record for: ')
	while duration <= 0:
		duration = input('Incorrect amount of time. Try again: ')

	#Get the white balance level
	balance = raw_input("""Choose a white-balance setting (auto, off, sunlight, 
		cloudy, shade, tungsten, fluorescent, incandescent, flash, horizon): """)
	while (balance != 'auto' and balance != 'off' and balance != 'sunlight' and
			balance != 'cloudy' and balance != 'shade' and balance != 'tungsten' and
			balance != 'fluorescent' and balance != 'incandescent' and
			balance != 'flash' and balance != 'horizon'):
		balance = raw_input('Incorrect setting. Try again: ')
			
	#Get the brightness level
	brightness = input('Enter a brightness. Default is 50 (1 - 100): ')	
	while brightness > 100 or brightness < 0:
		brightness = input('Incorrect brightness. Enter a number between 1 and 100: ')

	#Get how long the user wants to delay before starting image capture
	delay = input('How many minutes would you like to delay before recording: ')
	while delay < 0:
		delay = input('Incorrect amount of time. Try again: ')

	#Initialize camera and set options
	camera = picamera.PiCamera()
	camera.resolution = (width, height)
	camera.awb_mode = balance
	camera.brightness = brightness

	#Demo image
	demo = raw_input('Type y if you would like a demo picture: ')
	if demo == 'y':
		camera.capture('demo.jpg')
		print('demo.jpg saved locally.')
		confirm = raw_input('Type y if you would like to redo the settings.')
	else: 
		confirm = ''

#Delay before starting
time.sleep(60*delay)

#Update savepath
SAVEPATH = SAVEPATH + name

#If the directory does not exist, create it
try:
	os.makedirs(SAVEPATH)
except OSError:
	if not os.path.isdir(SAVEPATH):
		raise

totalframes = fpm*duration
framecount = 0

#Image render loop
while framecount < totalframes:
	framecount += 1
	camera.capture(SAVEPATH + '/' + name + str(framecount) + '.jpg')
	percent = framecount/totalframes
	print('Image ' + name + str(framecount) + '.jpg has been saved to ' +
		SAVEPATH + '.               ' + str(framecount) +'/' + str(totalframes) )
	time.sleep(60.0/fpm)
	

