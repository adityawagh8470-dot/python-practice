class vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class car(vehicle):
    def __init__(self, brand, price, model):
        self.model = model
        super().__init__(brand, price)

    def display(self):
        print("brand : ", self.brand)
        print("price: ", self.price)
        print("model :", self.model)

c1 = car("bmw", 4000000, 2019)
c1.display()

