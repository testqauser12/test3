import sys
class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
if sys.argv[3] == mustang:
    print (sys.argv[3].wheels)

class Cat(object):

    poroda = 5

    def __init__(self, makes, models):
        self.makes = makes
        self.models = models

kitty = Cat('de', 'dew')
if sys.argv[3] == kitty:
    print (sys.argv[3].poroda)
