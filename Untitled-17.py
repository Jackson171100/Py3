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

print(var1.pop())
var1.push("b")
var1.push("c")

print(var1.pop())


    