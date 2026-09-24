class Menu:
    def __init__(self):
        self.menu_items = []

    def add_to_menu(self, menu_item):
        self.menu_items.append(menu_item)

    def remove_from_menu(self, menu_item):
        self.menu_items.remove(menu_item)

    def all_items(self):
        return list(self.menu_items)

    def find_by_id(self, item_id):
        for menu_item in self.menu_items:
            if menu_item.id == item_id:
                return menu_item
        raise ValueError("menu item not found")