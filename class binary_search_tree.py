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
            self.root=Node
        else:
            spcx=self.left
            #intc=self.right 
            while True:
                if spcx==True:
                    value-1
                #if intc==True:
                    #value+1
