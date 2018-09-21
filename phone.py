class Name:
    def __init__(self, name, color, price):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        return f'телефон: {self.name}, {self.color} - {self.price}.'


    @classmethod
    def import_from_file(cls, file_name):
        items_source = open(file_name, 'r', encoding='utf-8').readlines()
        items_source = list(map(lambda x: x.replace('\n', '').split(', '), items_source))
        items_schema = items_source.pop(0)
        items_source_as_dict = list(map(lambda x: dict(zip(items_schema, x)), items_source))
        items = []
        for item_dict in items_source_as_dict:
            _item = cls(**item_dict)
            items.append(_item)
        return items


class Characteristic(Name):

    def __init__(self, number, camera, *args, **kwargs):
        self.number = number
        self.camera = camera


    def __str__(self):
            return f'характеристика: {self.number}, {self.camera}.'



class Accessories(Name):

    def __init__(self, name, color, price, *args, **kwargs):
        self.name = name
        self.color = color
        self.price = price

    def __str__(self):
        if self.price:
            return f'аксессуары: {self.name}, ({self.color}) - {self.price} руб.'


