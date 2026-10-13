class vehicle:
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

class car(vehicle):
    def __init__(self, brand, price, model):
        super().__init__(brand, price)
        self.model = model

    def display(self):
        print("brand: ", self.brand)
        print("price: ", self.price)
        print("model: ", self.model)

s1= car("bmw", 780000, 2019)
s1.display()
