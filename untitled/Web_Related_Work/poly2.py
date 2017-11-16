class Car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        raise NotImplementedError("Subclass must implement abstract method")

    def stop(self):
        raise NotImplementedError("Subclass must implement abstract method")


class Sportscar(Car):

    def __init__(self, name):
        super().__init__(name=name)

    def drive(self):
        return 'Sportscar driving!'

    def stop(self):
        return 'Sportscar breaking!'


class Truck(Car):
    def __init__(self, name, height):
        super().__init__(name=name)
        self.height = height

    def drive(self):
        return 'Truck driving slowly because heavily loaded.'

    def stop(self):
        return 'Truck breaking!'


cars = [Truck('Bananatruck,', 1),
        Truck('Orangetruck', 3),
        ]

for Truck in cars:
    print("{}".format(Truck.height))
