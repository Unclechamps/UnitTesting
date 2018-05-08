# User should be able to create a shopping list
# User should be able to add grocery items to a particular shopping list
# User should not be able to create duplicate lists (lists that have the same shop name)
# User should not be able to add duplicate items to a list
# User should be able to display shopping lists along with items of each list
# User should be able to supply the quantity of each item in the shopping list
# User should be able to remove items from the shopping list

from groceries import Store
from groceries import GroceryItems
from groceries import ShoppingList
import unittest


class TestGroceries(unittest.TestCase):

    def setUp(self):
        self.shopping_list = ShoppingList()
        self.store = Store("Test Store")
        self.grocery_item = GroceryItems("Test Grocery", 10)

    def testAddStore(self):
        self.shopping_list.addStore('Target')
        self.assertEqual('Target', self.shopping_list.store[0])


    def tearDown(self):
        print("TEAR DOWN!")

if __name__ == '__main__':
    unittest.main()
