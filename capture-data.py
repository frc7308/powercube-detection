import cv2
import time
import os
import datetime
import time

camera_port = 0
camera = cv2.VideoCapture(camera_port)
delay = 0.5

def get_image():
  retval, im = camera.read()
  return im

ts = time.time()
directory = "images_" + datetime.datetime.fromtimestamp(ts).strftime('%Y-%m-%d')
count = 1
dirfound = False
while not dirfound:
    if not os.path.exists(directory + "_" + str(count)):
        os.makedirs(directory + "_" + str(count))
        directory = directory + "_" + str(count)
        dirfound = True
    else:
        count += 1

i = 0
while (True):
    camera_capture = get_image()
    cv2.imwrite(directory + "/box_" + str(i) + ".png", camera_capture)
    print("Took image #" + str(i))
    i += 1
    time.sleep(0.5)

if not os.path.exists(directory):
    os.makedirs(directory)