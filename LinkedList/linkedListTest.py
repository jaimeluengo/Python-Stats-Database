
'''HW3 Q2 Jaime Luengo Rozas
Test case file for methods in linkedlist'''
from linkedList import LinkedList

#isEmpty: check if returns true for empty list and false for none
#Also check size and printlist method for empty list
ltest = LinkedList()
print "For an empty linkedlist",
ltest.printList()
print "isEmpty returns %r  and size is %d"%(ltest.isEmpty(),ltest.size())

#Now I add a new Node and check if it is there, and if isEmpty returns false
#Also I test if printList is working correctly for one element
ltest.add(400)
print "After addidng 400 the list becomes",
ltest.printList()
print("and isEmpty returns %r " % ltest.isEmpty())

#add 4 more elements and check if the size is 5
#Also I test if printList is working correctly for several elements
ltest.add(500)
ltest.add(300)
ltest.add(300)
ltest.add(700)
print "\nThe size of the list",
ltest.printList()
print("is %d " % ltest.size())

#Searching the element 500 should return true and 123 false

print "\nFor the list",
ltest.printList()
print(":\nnumber 500 is included? %r"
      "\nnumber 123 is included? %r" % (ltest.search(500),ltest.search(123)))

#removing the first element, the last one, and one in between
print "\nAfter removing the first element in the list",
ltest.printList()
ltest.remove(700)
print "becomes",
ltest.printList()
print "\nAfter removing the last element in the list becomes ",
ltest.remove(400)
ltest.printList()
print "\nAfter removing an element in between 500 the list becomes ",
ltest.remove(500)
ltest.printList()

#Test if findAll finds all the 300s in the list. Test for a non-existing element
ltest.add(500)
ltest.add(700)
ltest.add(500)
ltest.add(300)
ltest.add(300)
print "\n\nFor the list: ",
ltest.printList()
print " is element %d found?" % 300
ltest.findAll(300)
print "What about %d?" % 123
ltest.findAll(123)

#Test insert method for the first position,last and in between
print "\nFor the list: ",
ltest.printList()
print " after inserting %d at position %d it becomes:" % (800,0),
ltest.insert(0,800)
ltest.printList()
print "\nAfter inserting %d at position %d it becomes" % (350,ltest.size()-1)
ltest.insert(ltest.size()-1,350)
ltest.printList()
print "\nAfter inserting %d at position %d it becomes:" % (240,3),
ltest.insert(3,240)
ltest.printList()

#Test pop by popping element at position, last and middle
print "\n\nFor the list: ",
ltest.printList()
print " after popping element %d at position %d it becomes:" %(ltest.popAtIndex(0),0),
ltest.printList()
print "\nAfter popping element %d at position %d it becomes" %(ltest.popAtIndex(ltest.size()-1),ltest.size()),
ltest.printList()
print "\nAfter popping element %d at position %d it becomes:" %(ltest.popAtIndex(3),3),
ltest.printList()

#Test append for an empty list and a normal one
ltest2 = LinkedList()
print "\n\nWhen appending an element %d to an empty list it becomes: " %4,
ltest2.appendLast(4)
ltest2.printList()
print "\nAppending %d to this list, it becomes:" %6,
ltest2.appendLast(6)
ltest2.printList()
