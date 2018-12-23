import requests
import cv2
import json
import numpy as np
import urllib.request as urllib
import matplotlib.pyplot as plt
from minimal_object_detection_lib import *

import io
import random

import time

result = None
output = None

# Helper functions
def PostFile(filename, fileObj, Host, Port = 20000):
    site = 'http://' + Host + ':' + str(Port) + '/MachineImageMessageApi'
    file = {'image': (filename, fileObj)}
    data = {}
    request = requests.post(site, files=file, data=data)
    
def PostImage(filename, image, Host, Port = 20000):
    retval, content = cv2.imencode('.jpg', image)
    fileObj = io.BytesIO(content)
    PostFile(filename, fileObj, Host, Port)
    
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
    PostImage(filename, img, Host, Port)




def PostResult(Host, Payload, port = 20000, Uri = None):
    if Uri == None:
        Uri = "http://" + Host + ":" + str(port) + "/MachineMessageApi"
    r = requests.post(Uri, json=Payload)
    return r.text

def ResultToJson(result):
    result = str(result).replace("'", '"')
    result = json.loads(result)
    return result

def getImageFromShotUri(url):
    imgResp = urllib.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()),dtype=np.uint8)
    img = cv2.imdecode(imgNp,-1)
    return img

def PyPlot(image):
    plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
    plt.show()

def ImShow(window, image, millis = 0):
    val = 0
    count = 0
    while val != ord('q'):
        cv2.imshow(window, image)
        val = cv2.waitKey(30)
        count += 1
        if (millis != 0 and (count * 30) > millis):
            break
    cv2.destroyAllWindows()

class DrawProcess:
    Payload = ""
    AlgorithmInSyntax = ""
    Stopper = True
    
    def SetAlgorithmInSyntax(self, algorithmInSyntax: str):
        self.AlgorithmInSyntax = algorithmInSyntax
    
    def SetPayload(self, payloadString : str):
        self.Payload = payloadString
        
    def Draw(self, runOnce:bool = True, infinite:bool = False, limit: int = 1):
        self.Stopper = False
        c = 0
        
        if runOnce == True:
            limit = 1
            infinite = False
        
        while (c < limit):
            globals()["output"] = None
            globals()["result"] = None
            globals()["ExecuteDevelopmentCode"] = False

            # exec(self.AlgorithmInSyntax, globals())
            # exec(self.Payload, globals())
            
            if (globals()["ExecuteDevelopmentCode"] == True):
                print("Hello, development code executing")
                # Result logic START
                globals()["result"] = tfnet.return_predict(imageSrc)
                globals()["output"] = ResultToJson(str(result))
                # Result logic END
                print("Development code output ends here")

            if infinite == False:
                c += 1
            
            if self.Stopper == True:
                break
            
            time.sleep(0.5)

        return output
    
    def Stop(self):
        self.Stopper = True

