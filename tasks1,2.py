class _Technic:
    __slots__ = ('title', 'price', 'availability')

    def __init__(self, title:str, price: int, availability: bool):
        self.title = title
        self.price = price
        self.availability = availability

    def category(self):
        return 'cheap' if 0 <= self.price <= 20000 else 'expensive'

    def __eq__(self, other_tech):
        return len(self.title) == len(other_tech.title)
