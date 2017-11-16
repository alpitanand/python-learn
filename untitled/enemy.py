import random


class Enemy:
    def __init__(self, name='Enemy', hit_points=10, lives=1):
        self.name = name
        self.hit_points = hit_points
        self.lives = lives
        self.alive = True

    def take_damage(self, damage):
        remaining_point = self.hit_points - damage
        self.hit_points = remaining_point
        if remaining_point > 0:
            print(remaining_point)
            print("I took {} damage".format(self.name))
        else:
            self.alive = False
            if self.lives > 0:
                print("{} Taken {} damage".format(self.name, self.hit_points))

    def __str__(self):
        return "Name: {}, Lives:{}, Hit-points :{}".format(self.name, self.lives, self.hit_points)


class Troll(Enemy):
    def __init__(self, name):
        super(Troll, self).__init__(name=name, hit_points=50, lives=5)

    def grunt(self):
        print("{} stomp you".format(self.name))


class Vampire(Enemy):
    def __init__(self, name):
        super().__init__(name=name, hit_points=12, lives=1)

    @staticmethod
    def dodges(self):
        if random.randint(1, 3) == 3:
            print("Dodges")
            return True
        else:
            return False

    def take_damage(self, damage):
        if not self.dodges(self):
            super().take_damage(damage=damage)


class VampireKing(Vampire):
    def __init__(self, name):
        super().__init__(name=name)
        self.hit_points = 140

    def take_damage(self, damage):
        super().take_damage(damage=damage//4)
