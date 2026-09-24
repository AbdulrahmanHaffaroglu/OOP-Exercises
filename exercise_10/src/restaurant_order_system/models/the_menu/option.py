class Option:
    def __init__(self, name, price):
        if price <= 0:
            raise ValueError("extra options should cost")
        
        self.name = name
        self.price = price


class OptionGroup:
    def __init__(self, options=None, is_required=False):
        self.options = options or []
        self.is_required = is_required

    def add_option(self, extra):
        self.options.append(extra)