#from networktables import NetworkTables
from infer import classify
import cv2
import numpy as np
import time

center = (640, 360)
'''
while (True):
    print(str(time.time()) + " - " + str(classify("PowerCubeNet.caffemodel", "deploy.prototxt", "img.jpg")))

# FOV - 60 deg
'''
camera_port = 0
filename = "img.png"
capturing = True

camera = cv2.VideoCapture(camera_port)

def get_image():
  _, img = camera.read()
  return img

result = ((0, 0), (0,0), 0.0)

while (capturing):
  camera_capture = get_image()
  camera_capture = cv2.resize(camera_capture, (640, 360))
  result = classify("PowerCubeNet.caffemodel", "deploy.prototxt", np.asarray(camera_capture))
  try:
    cv2.rectangle(camera_capture, result[0], result[1], (0, 255, 0), 4)
  except:
    print("oof")

  cv2.imwrite("test.jpg", camera_capture)
  
  print(result)

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