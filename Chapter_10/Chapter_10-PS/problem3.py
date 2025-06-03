from random import randint

class Train:
    def __init__(self, trainNo):
        self.trainNo = trainNo
        
    def book(self, fro, to):
        print(f"Booking a ticket from {fro} to {to} on train number {self.trainNo}")
        
    def getStatus(self):
        print(f"Train {self.trainNo} is running on time.")
    
    def getFare(self, fro, to):
        print(f"The fare from {fro} to {to} on train number {self.trainNo} is {randint(100, 500)} rupees.")

t = Train("12345")
t.book("Delhi", "Mumbai")
t.getStatus()
t.getFare("Delhi", "Mumbai")