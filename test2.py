import sys
class Car(object):

    wheels = 4

    def __init__(self, make, model):
        self.make = make
        self.model = model

mustang = Car('Ford', 'Mustang')
if sys.argv[2] == 1:
    print ('test1')

class Cat(object):

    poroda = 5

    def __init__(self, makes, models):
        self.makes = makes
        self.models = models

kitty = Cat('de', 'dew')
if sys.argv[2] == 2:
    print ('test2')
