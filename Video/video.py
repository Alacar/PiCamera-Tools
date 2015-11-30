import picamera
import time

name = raw_input('Enter a video name: ')
length = input('Enter a video length in seconds: ')

camera = picamera.PiCamera()

camera.start_preview()
camera.start_recording(name + '.h264')

time.sleep(length)

camera.stop_preview()
camera.stop_recording()
