import time

class DrawProcess:
    Payload = ""
    Stopper = True
    
    def SetPayload(self, payloadString : str):
        self.Payload = payloadString
        
    def Draw(self, runOnce:bool = True, infinite:bool = False, limit: int = 1):
        self.Stopper = False
        c = 0
        
        if runOnce == True:
            limit = 1
            infinite = False
        
        while (c < limit):
            exec(self.Payload)
            
            if infinite == False:
                c += 1
            
            if self.Stopper == True:
                break
            
            time.sleep(0.5)
        
    def Stop(self):
        self.Stopper = True