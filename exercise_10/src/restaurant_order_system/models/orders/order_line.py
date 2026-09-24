class OrderLine:
    def __init__(self, menu_item, quantity=1, options=None):
        if quantity <= 0:
            raise ValueError("quantity must be greater than zero")

        self.menu_item = menu_item
        self.quantity = quantity
        self.options = list(options or [])

        option_group = getattr(menu_item, "sizes", None) or getattr(menu_item, "extras", None)
        if option_group is None:
            if self.options:
                raise ValueError("this menu item does not support options")
        else:
            invalid_options = [option for option in self.options if option not in option_group.options]
            if invalid_options:
                raise ValueError("one or more options are not available for this menu item")
            if option_group.is_required and not self.options:
                raise ValueError("a required option must be selected")

        self.unit_price = menu_item.price + sum(option.price for option in self.options)

    def matches(self, menu_item, options):
        return self.menu_item == menu_item and self.options == list(options or [])

    @property
    def total_price(self):
        return self.unit_price * self.quantity