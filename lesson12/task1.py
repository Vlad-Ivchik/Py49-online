class Item:
    def __init__(self, name, store, price):
        self.__name = name
        self.__store = store
        self.__price = price

    @property
    def name(self):
        return self.__name

    @property
    def store(self):
        return self.__store

    @property
    def price(self):
        return self.__price

    def __str__(self):
        return f"Name: {self.name}, Store: {self.store}, Price: {self.price} rub."


class Warehouse:
    def __init__(self):
        self.__items = []

    @property
    def items(self):
        return self.__items

    def add_item(self, item):
        self.__items.append(item)

    def __getitem__(self, index_or_name):
        if isinstance(index_or_name, int):
            if 0 <= index_or_name < len(self.__items):
                return self.__items[index_or_name]
        elif isinstance(index_or_name, str):
            items_with_name = []
            for item in self.__items:
                if item.name == index_or_name:
                    items_with_name.append(item)
            return items_with_name
        return None

    def sort(self, key=None, reverse=False):
        self.__items.sort(key=key, reverse=reverse)

    def __add__(self, other):
        if isinstance(other, Warehouse):
            total_price = sum(item.price for item in self.__items) + sum(item.price for item in other.__items)
            return total_price
        else:
            raise TypeError


item1 = Item("Phone", "Store1", 10000)
item2 = Item("Fridge", "Store2", 15000)
item3 = Item("Phone", "Store1", 17000)
item4 = Item("TV", "Store3", 12000)

warehouse = Warehouse()

warehouse.add_item(item1)
warehouse.add_item(item2)
warehouse.add_item(item3)
warehouse.add_item(item4)

