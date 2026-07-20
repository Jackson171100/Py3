import littlesister
class queue:
    def __init__(self):
        self.linklist=littlesister.Linklist()
    def enqueue(self,value):
        self.linklist.append(value)
    def dequeue(self):
        return self.linklist.remove(0)
var1=queue()
var1.enqueue("a")
var1.dequeue()     
    