class Kettle(object):

    power_source = "electricity"

    def __init__(self, make, price):
        self.make = make
        self.price = price
        self.on = False

    def switch_on(self):
        if not self.on:
            self.on = True


Hamilton = Kettle("Hamilton", 12.99)
Kenwood = Kettle("Kenwood", 8.99)
print(Kenwood.make)
print(Kenwood.price)
print(Kenwood)
print(type(Kenwood))
print("Models: {0.make}, {0.price}, {1.make}, {1.price}".format(Kenwood, Hamilton))
print(Hamilton.on)
Hamilton.switch_on()
print(Hamilton.on)
Kettle.switch_on(Kenwood)
print(Kenwood.on)
Kenwood.power = 1.5
print(Kenwood.power)
print("*" * 80)
Kettle.power_source = "atomic"
print(Kettle.power_source)
print(Kenwood.power_source)
print(Hamilton.power_source)
print(Kettle.__dict__)
print(Kenwood.__dict__)
print(Hamilton.__dict__)
