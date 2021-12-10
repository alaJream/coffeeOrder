class Person():
    def __init__(self, name, fav_drink):
        self.name = name
        self.fav_drink = fav_drink

    def my_order(self):
        return Order(self.fav_drink, self)

class Order():
    def __init__(self, type, person):
        self.type = type
        self.person = person
    
    def to_string(self):
        return f"{self.person.name} orders: {self.type}"
        

class Coffeebar():
    def __init__(self, name, barista):
        self.name = name
        self.orders = []
        self.barista = barista

    def place_order(self, order):
        self.orders.append(order)

    def process_orders(self):
        for order in self.orders:
            print(f'{self.barista.greeting} {order.to_string()}')

class Barista(Person):
    def __init__(self, name, fav_drink, greeting):
        super().__init__(name, fav_drink)
        self.greeting = greeting

if __name__ == '__main__':
    amy = Person('Amy', 'Coffee')
    bob = Person('Bob', 'Tea')
    cat = Person('Cat', 'Milk')
    barista = Barista('Kevin', 'Coffee', "Hey dude!")
    coffeebar = Coffeebar('Philz', barista)
    coffeebar.place_order(amy.my_order())
    coffeebar.place_order(bob.my_order())
    coffeebar.place_order(cat.my_order())
    coffeebar.process_orders()

# Amy.my_order().to_string()
# Bob.my_order().to_string()
# Cat.my_order().to_string()
