

class ShoppingCart:
    
    def __init__(self):
        self.__items = []

    def add_item(self, item):
        self.__items.append(item)

    def print_cart(self):
        for item in self.__items:
            print(item)

    @classmethod
    def create_cart_from_items(cls, items):
        sc = ShoppingCart()
        for item in items:
            sc.add_item(item)
        return sc


# shopping_cart = ShoppingCart()

# shopping_cart.add_item("animal crackers")
# shopping_cart.print_cart()

sc = ShoppingCart.create_cart_from_items(['carrots','apples','eggs'])

