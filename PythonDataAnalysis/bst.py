import pandas as pd

class bst:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def is_bst_(self):
        return self.data==1?True:False
        return self.left==None?(return self.right.is_bst()):((self.left.data<self.data)&&(self.right==None?(return self.left.is_bst()):(self.data < self.right.data?True:False)))

    def is_bst(self):
        return self.right.is_bst() if self.left == None else


df=pd.DataFrame(fff)


