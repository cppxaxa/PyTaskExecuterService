import requests
import cv2
import io
import numpy as np
import random

def PostFile(filename, fileObj, Host, Port = 20000):
    site = 'http://' + Host + ':' + str(Port) + '/MachineImageMessageApi'
    file = {'image': (filename, fileObj)}
    data = {}
    request = requests.post(site, files=file, data=data)
    
def PostImage(filename, image, Host, Port = 20000):
    retval, content = cv2.imencode('.jpg', image)
    fileObj = io.BytesIO(content)
    PostFile(filename, fileObj, 'localhost', 20000)
    
def GenerateDummyImage():
    img = np.zeros((400,550,3), np.uint8)
    x = random.randint(0,200)
    y = random.randint(0,200)
    s = random.randint(0,100)
    cv2.rectangle(img,(250 + x,100 + y),(300 + x + s,150 + y + s),(255,255,255),3)
    x = random.randint(0,200)
    y = random.randint(0,200)
    s = random.randint(0,100)
    cv2.rectangle(img,(250 + x,100 + y),(300 + x + s,150 + y + s),(0,255,0),3)
    return img

def PostDummyImage(Host, Port = 20000):
    filename = 'shot.jpg'
    img = GenerateDummyImage()
    PostImage(filename, img, 'localhost', 20000)


PostDummyImage('localhost', 20000)






