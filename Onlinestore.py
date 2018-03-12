''' Question 1 HW3 Jaime Luengo Rozas jl3752
This program implements Class Grocery, which contains a constructor and three 
methods: buildInventory(), viewInventory() and checkOut(), to handle a small online 
grocery store's inventory operations and check out transactions'''

class Grocery:
    def __init__(self):
        self.inventory = {}
    def buildInventory(self,inv):
        self.inventory = inv
    def viewInventory(self):
        if(len(self.inventory) == 0):
            print("The inventory is empty. Put an order ASAP.")
        else:
            print("Item\tStock\tPrice")
            print("-"*25)
            for it in self.inventory:
                print("%s\t %d\t%.2f"%(it,self.inventory[it][0],
                                         self.inventory[it][1]))
            print("-"*25)
    def checkOut(self):
        buy = raw_input("Do you want to buy something?")
        if(buy.lower() == "yes" or buy.lower() == "y"):
            flag = True
            i=0
            invoice = []
            while(flag):
                item = raw_input("Enter an item to buy:")
                if(item in self.inventory):
                    qi = self.inventory.get(item)[0] #quantity of stock in inventory
                    if(qi>0):
                        qr = input("How many do you want?") #quantity requested
                        if(qr>qi):
                            print("Not enough in stock; we can "
                                  "only sell you %d item(s)." % qi)
                            stillbuy= raw_input("Do you still want to buy it?")
                            if(stillbuy.lower()=="yes" or stillbuy.lower()=="y"):
                                self.inventory.get(item)[0] = max(0,qi-qr)
                                invoice.append((item,min(qr,qi)))
                        else:
                            self.inventory.get(item)[0] = max(0,qi-qr)
                            invoice.append((item,min(qr,qi)))
                        
                if(item not in self.inventory or qi == 0):
                    print("Wrong item name or out of stock.")

                repeat = raw_input("Do you still want to buy something?")
                if(repeat.lower() == "no" or repeat.lower() == "n"):
                    flag = False
                            
        else:
            print("Goobye.")

        if(len(invoice)==0):
            print("Goodbye")
        else:
            print("Item\tQuantity\tPrice\t Subtotal")
            print("-"*50)
            total = 0
            for it in invoice:
                price = self.inventory.get(it[0])[1]
                print("%s\t %d\t\t%.2f\t%.2f"%(it[0],it[1],price,price*it[1]))
                total+= price*it[1]
            print("-"*50)
            print("Please pay $ %.2f \n\nGoodbye." % total)
    
