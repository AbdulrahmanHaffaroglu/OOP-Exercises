from abc import abstractmethod, ABC

class MenuItem(ABC):

    id_num = 0

    def __init__(self, name, description, price, is_available):
        self.id = f"{MenuItem.id_num:03d}"
        MenuItem.id_num += 1
        self.name = name
        self.description = description
        self.price = price
        self.is_available = is_available
        
    