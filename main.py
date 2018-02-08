#from networktables import NetworkTables
from infer import classify
import cv2
import numpy as np
import time

center = (640, 360)

while (True):
    print(str(time.time()) + " - " + str(classify("PowerCubeNet.caffemodel", "deploy.prototxt", "img.jpg")))

# FOV - 60 deg

camera_port = 0
ramp_frames = 30
filename = "img.png"
capturing = True

camera = cv2.VideoCapture(camera_port)
 
def get_image():
  _, img = camera.read()
  return img

for i in xrange(ramp_frames):
  temp = get_image()

while (capturing):
  camera_capture = get_image()
  print(classify("PowerCubeNet.caffemodel", "deploy.prototxt", camera_capture))

del(camera)

'''
def valueChange(table, key, value, isNew):
    if (key === "enabled" & value == True) {
        print("wow")
    }

NetworkTables.initialize(server='10.73.8.2')
table = NetworkTables.getTable("jetson")

table.addEntryListener(valueChange)

table.putNumber('rotate', 1.0)
'''