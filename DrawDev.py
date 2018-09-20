from darkflow.net.build import TFNet
import cv2
import json

import time

result = None
output = None

# Helper functions

def ResultToJson(result):
    result = str(result).replace("'", '"')
    result = json.loads(result)
    return result

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

            exec(self.AlgorithmInSyntax, globals())
            exec(self.Payload, globals())
            
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