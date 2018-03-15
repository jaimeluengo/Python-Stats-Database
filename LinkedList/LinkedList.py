''' Question 2 HW2 Jaime Luengo Rozas jl3752
.'''
from node import Node

class LinkedList:

    def __init__(self):
        self.head = None

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
        if(self.isEmpty()):
            print "[]",
        else:
            print "[ %d"% current.getData(),
            while current.getNext() is not None:
                current = current.getNext()
                print ",%d" % current.getData(),
            print "]",

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
                positions.append(index)
            current=current.getNext()
            index+=1
        if not found:
             print("element was not found")
        else:
             print(("%d is found %d time(s) at positions "+str(positions))
                   %(element,len(positions)))

    def insert(self, position, element):
        current = self.head
        node_new = Node(element)
        for i in range(1,position):
            current = current.getNext()
        if position == 0:
            node_new.setNext(self.head)
            self.head = node_new
        else:
            node_new.setNext(current.getNext())
            current.setNext(node_new)

    def popAtIndex(self,position):
        current = self.head
        if(position==0):
            val = current.getData()
            self.head=self.head.getNext()
            return val
        else:
            for i in range(1,position):
                current = current.getNext()
            val = current.getNext().getData()
            current.setNext(current.getNext().getNext())
            return val

    def appendLast(self,element):
        current = self.head
        node_last = Node(element)
        if(self.isEmpty()):
            self.head = node_last
        else:
            while current.getNext()!=None:
                 current = current.getNext()
            current.setNext(node_last)
