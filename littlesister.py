class Node:
    def __init__(self,value,next):
        
        self.value=value
        self.next=next
class Linklist:
    def __init__(self):
        self.root=None
    def append(self,val):
        var1=self.root
        if self.root==None:
            self.root=Node(val,None)
            return
        while var1.next!=None:
             var1=var1.next
        var2=Node(val,None)
        var1.next=var2    
    def get(self,index):
        var1=self.root
        if index==0:
            return var1.value
        for i in range(index):
                
            var1=var1.next  
        return var1.value 
    def remove(self,index):
        if index==0:
            var6=self.root.value
            self.root=None
            return var6
        var1=self.root
        print(index)
        for i in range(index-1):
            print(i)    
            var1=var1.next
            
        var3=var1.next.value
          
        var1.next=var1.next.next
        return var3
    def length(self):
        var5=0
        var1=self.root
        if self.root==None:
            return 0
        while var1!=None:
            var5+=1
            var1=var1.next 
        return var5
var4=Linklist()
var4.append(1)
var4.append(2)
var4.append(3)
var4.append(4)
var4.append(5)
var4.length
for i in range(var4.length()-1):
    print(var4.get(i))



        