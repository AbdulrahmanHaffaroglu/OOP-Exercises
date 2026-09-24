from .menu_item import MenuItem
from .option import OptionGroup


class Drink(MenuItem):
    def __init__(self, name, description, price, availability, sizes=None):
        super().__init__(name, description, 0, availability)
        self.sizes = OptionGroup(sizes, is_required=True)

    def add_sizes(self, new_sizes):
        for size in new_sizes:
            self.sizes.add_option(size)