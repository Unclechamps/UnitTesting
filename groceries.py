#Groceries List

class ShoppingList():
    def __init__(self):
        self.grocery_stores = []

    def addStore(self,store):
        found = False
        for the_store in self.grocery_stores:
            if the_store.store_name == store.store_name:
                print ("This store is already on the list.")
                found = True
        if found == False:
             self.grocery_stores.append(store)

class Store():
    def __init__ (self, store_name):
        self.store_name = store_name
        self.grocery_list = []

    def addItem(self, toBuy):
        self.grocery_list.append(toBuy)

    def __repr__(self):
        return f"{self.store_name}"

class GroceryItems():
    def __init__ (self, grocery_item, quantity, price):
        self.grocery_item = grocery_item
        self.quantity = quantity
        self.price = price

    def __repr__(self):
        return f"{self.grocery_item}, {self.quantity}"

#Input
shoppinglist = ShoppingList()
store1 = Store('Fiesta')
toBuy1 = GroceryItems('Milk', 4, 3.50)

store2 = Store('Walmart')
toBuy2 = GroceryItems('Soda', 2, 4.00)
toBuy3 = GroceryItems('Eggs', 5, 6.25)
toBuy4 = GroceryItems('Bread', 8, 10)

shoppinglist.addStore(store1)
shoppinglist.addStore(store2)

store1.addItem(toBuy1)
store2.addItem(toBuy2)
store2.addItem(toBuy3)
store2.addItem(toBuy4)
#
# print(shoppinglist.store[0].grocery_list)
# print(shoppinglist.store[1].grocery_list)
#
for i in range(0, len(shoppinglist.grocery_stores)):
    print (shoppinglist.grocery_stores[i])
    print (shoppinglist.grocery_stores[i].grocery_list)
