from .menu_item import MenuItem

class Dessert(MenuItem):
    def __init__(self, name, description, price, availability):
        super().__init__(name, description, price, availability)