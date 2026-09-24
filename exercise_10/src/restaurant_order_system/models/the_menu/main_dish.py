from .menu_item import MenuItem
from .option import OptionGroup


class MainDish(MenuItem):
    def __init__(self, name, description, price, availability, extras=None):
        super().__init__(name, description, price, availability)
        self.extras = OptionGroup(extras, is_required=False)

    def add_extras(self, new_extras):
        for extra in new_extras:
            self.extras.add_option(extra)