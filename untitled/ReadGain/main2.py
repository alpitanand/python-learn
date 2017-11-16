from enemy import Enemy, Troll, Vampire, VampireKing
random_monster = Enemy("Gupta", 12, 1)
print(random_monster)

random_troll = Troll("Pug")
print(random_troll)

brother = Troll("Kauwa")
print(brother)
brother.grunt()
brother.take_damage(51)

vamp = Vampire("Ujjwal")
print(vamp)

vampKing = VampireKing("ad")
print(vampKing)
