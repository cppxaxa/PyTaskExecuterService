import requests
import cv2
from io import BytesIO

def PostFile(site, filename, fileObj):    
    file = {'image': (filename, fileObj)}
    data = {}
    request = requests.post(site, files=file, data=data)

site = 'http://localhost:20000/MachineImageMessageApi'
filename = 'Banana.jpg'

img = cv2.imread(filename)
cv2.imshow('', img)
cv2.waitKey()



fileObj = open(filename, 'rb')
print(fileObj)
# PostFile(site, filename, fileObj)
