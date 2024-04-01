class Address:
    index = "152 000"
    city = "Ivanovo"
    street = "Chapaeva"
    house = "21"
    flat = "8"

    def __init__(self, index, city, street, house, flat):
        self.index = index
        self.city = city
        self.street = street
        self.house = house
        self.flat = flat

    def full_info(self):
        print(self.index, self.city, self.street, self.house, "-", self.flat)