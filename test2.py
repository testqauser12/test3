class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
print (mustang.wheels)

class Cat(object):

    poroda = 5

    def __init__(self, makes, models):
        self.makes = makes
        self.models = models

kitty = Cat('de', 'dew')
print (kitty.poroda)
