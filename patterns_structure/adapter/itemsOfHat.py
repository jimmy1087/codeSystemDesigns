#########################################################
# When 2 classes already work together ie:   ShoppingCart talking to Items
# And you need to have a 3rd class (Hat) acting as an Item
# You build an adapter
#########################################################

class Item:
    
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def itemName(self):
        return self.name
    
    def itemPrice(self):
        return self.price

class ShoppingCart:

    def __init__(self):
        self.items = []
    
    def addItemToShoppingCart(self, item):
        self.items.append(item)
    
    def printShoppingCarts(self):
        for item in self.items:
            print(item.itemName(), item.itemPrice())

###########

# Different class than Item
class Hat:

    def __init__(self, type, cat, price):
        self.type = type
        self.category = cat
        self.price = price

###########

class HatAdapter(Item):

    def __init__(self, type, category, price):
        self.hat = Hat(type, category, price)

    def itemName(self):
        return self.hat.type + " " + self.hat.category
    
    def itemPrice(self):
        return self.hat.price

#########################################################

s = ShoppingCart()
h1 = HatAdapter("Golden hat", "soft", 100)
h2 = HatAdapter("Silver hat", "medium", 200)
h3 = HatAdapter("Brown hat", "heavy", 300)
s.addItemToShoppingCart(h1)
s.addItemToShoppingCart(h2)
s.addItemToShoppingCart(h3)

s.printShoppingCarts()