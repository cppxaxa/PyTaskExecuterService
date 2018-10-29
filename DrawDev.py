import requests
import cv2
import json
import numpy as np
import urllib.request as urllib
import matplotlib.pyplot as plt
from minimal_object_detection_lib import *

import time

result = None
output = None

# Helper functions

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

