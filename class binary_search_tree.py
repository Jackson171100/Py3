class Node:
    def __init__(self,left,right,value):
        self.left=left
        self.right=right
        self.value=value
class binary_search_tree:
    def __init__(self):
        self.root=None
    def append(self,value):
        if self.root==None:
            self.root=Node(None,None,value)
        else:
            spcx=self.root
            #intc=self.right 
            while True:
                if value>spcx.value:
                    if spcx.right:
                        spcx=spcx.right
                    else:
                        spcx.right=Node(None,None,value)
                        break
                else:
                    if spcx.left:
                        spcx=spcx.left
                    else:
                        spcx.left=Node(None,None,value)
    def search(self,value):                        
            mu=self.root
            while True:
                if mu.value==value:
                    return True
                if value>mu.value:
                    if mu.right==None:
                        return False
                    else:
                        mu=mu.right
                else:
                    if mu.left==None:
                        return False
                    else:
                        mu=mu.left
var7767=binary_search_tree()
var7767.append(1)
var7767.append(2)
var7767.append(3)
var7767.append(4)
print(var7767.search(5))