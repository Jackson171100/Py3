import littlesister
class stack:
    def __init__(self):
        self.linklist=littlesister.Linklist() 
    def push(self,value):
        self.linklist.append(value)
    def pop(self):
        return self.linklist.remove(self.linklist.length()-1)
var1=stack()
var1.push("a")
var1.pop()


    