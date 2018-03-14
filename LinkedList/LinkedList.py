''' Question 2 HW2 Jaime Luengo Rozas jl3752
.'''

class LinkedList:

    def __init__(self):
        self.head = Node

    def isEmpty(self):
        return self.head == None
    
    def add(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count+=1
            current = current.getNext()
        return count
    def search(self,element):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == element:
                found = True
            else:
                current=current.getNext()
        return found

    def remove(self, element):
        current = self.head
        previous = None
        found = False
        while current != None and not found:
            if current.getData() == element:
                found =True
            else:
                previous=current
                current=current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

    #print all elements of the linkedlist        
    def printList(self):
        current = self.head
        while current!= None:
              print( current.getData(), )

    #find how many times a given paramenters appears in a linkedlist
    #and in what possitions
    def findAll(self,element):
        current = self.head
        positions = []
        index=0
        found = False
        while current != None:
            if current.getData() == element:
                found = True
                positions.add(index)
            else:
                current=current.getNext()
        if not found:
             print("element was not found")
        else:
             print(("%d is found %d time(s) at positions"+positions)
                   %element,len(positions))

    def insert(self, position, element):
        current = self.head
        node_new = Node(element)
        for i in range(1,position):
            current = current.getNext()
        if postion == 0:
            node_new.setNext(current.getNext())
            self.head = node_new
        else:
            node_new.setNext(current.getNext())
            current.setNext(node_new)

    def popAtIndex(self,position):
        if(position==0):
            self.head=self.head.getNext()
        else:
            for i in range(1,position):
                current = current.getNext()
            val = current.getNext().getData()
            current.setNext(current.getNext().getNext())
            return val

    def appendLast(self,element):
        current = self.head
        node_last = Node(element)
        while current.getNext()!=None:
             current = current.getNext()
        current.setNext(node_last)
        
    class Node:
        def __init__(self,initdata):
            self.data = inidata
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
