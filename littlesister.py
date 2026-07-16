class Node:
    def __init__(self,value,next):
        
        self.value=value
        self.next=next
class Linklist:
    def __init__(self):
        self.root=None
    def append(self,val):
        var1=self.root
        while var1.next!=None:
             var1=var1.next
        var2=Node(val,None)
        var1.next=var2    
    def get(self,index):
        for i in range():
        
        