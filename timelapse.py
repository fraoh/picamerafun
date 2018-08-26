from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (1024, 768)
stop = False

while not stop:
#for i in range(60):
    camera.capture('image{0:04d}.jpg'.format(i))
    sleep(60)
