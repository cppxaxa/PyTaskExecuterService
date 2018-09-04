import time

class DrawProcess:
    Payload = ""
    AlgorithmInSyntax = ""
    Stopper = True
    
    def SetAlgorithmInSyntax(self, algorithmInSyntax: str):
        self.AlgorithmInSyntax = algorithmInSyntax
    
    def SetPayload(self, payloadString : str):
        self.Payload = payloadString
        
    def Draw(self, runOnce:bool = True, infinite:bool = False, limit: int = 1):
        output = 10
        
        self.Stopper = False
        c = 0
        
        if runOnce == True:
            limit = 1
            infinite = False
        
        while (c < limit):
            exec(self.AlgorithmInSyntax)
            exec(self.Payload)
            
            if infinite == False:
                c += 1
            
            if self.Stopper == True:
                break
            
            time.sleep(0.5)
            
        return output
    
    def Stop(self):
        self.Stopper = True