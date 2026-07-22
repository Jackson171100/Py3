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
