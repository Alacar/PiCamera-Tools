import picamera

camera = picamera.PiCamera()
camera.start_preview()

input('Press enter to stop')
camera.stop_preview()
