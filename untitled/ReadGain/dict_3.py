fruit = {"orange": "A sweet orange",
         "apple": "good for making cedar",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit growing in branches",
         "lime": "a sour,green fruit"}

print(fruit)

veg = {"cabbage": "every child favorite",
       "sprouts": "mmmmm, lovely",
       "spinach": "can i have some more fruit"}

print(veg)

veg.update(fruit)   # will not return a new dictionary use copy method instead
print(veg)
fruit2 = ["banana", "mango", "apple"]
fruit2.sort()  # this will mot return a new list
sorted(fruit)  # however this will

nice_and_nasty = fruit.copy()
nice_and_nasty.update(veg)
print(nice_and_nasty)
