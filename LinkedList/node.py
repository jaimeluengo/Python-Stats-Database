class Node:
        def __init__(self,initdata):
            self.data = initdata
            self.next = None

        #return the data of a node
        def getData(self):
             return self.data

        #return the reference to next node
        def getNext(self):
            return self.next

        #assign a new data value to the current node
        def setData(self, newdata):
            self.data = newdata

        #assign a new reference pointing to the next node
        def setNext(self,newnext):
            self.next = newnext
