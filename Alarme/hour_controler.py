from datetime import datetime

class UpDown():
    def __init__(self, start, end, now = datetime.now().strftime('%H')):
        self.start = start
        self.end = end - 1
        self.hora = int(now)
        
    def incremente(self):
        if(self.hora >= self.end):
            self.hora = self.start
        else:
            self.hora += 1
    
    def decremente(self):
        if(self.hora <= self.start):
            self.hora = self.end
        else:
            self.hora -= 1