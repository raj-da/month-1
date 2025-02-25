class Vehicle:
    def __init__(self, doors=None, color=None, tiers=None):
        self.doors = doors
        self.color = color
        self.tiers = tiers

    def engin(self):
        print("The engin sounds like a vehicles")


class Car(Vehicle):
    def __init__(self, doors=None, color=None, tiers=None):
        super().__init__(doors, color, tiers)

    def engin(self):
        print("The  engins sound like a cars")

    def __str__(self):
        return "This is a car object"
    
class Bike(Vehicle):
    def __init__(self, doors=None, color=None, tiers=None):
        super().__init__(doors, color, tiers)

    def engin(self):
        print("The  engins sound like a Bikes")

    def __str__(self):
        return "This is a Bike object"