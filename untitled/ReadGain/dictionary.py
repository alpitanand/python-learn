fruit = {"orange": "A sweet orange",
         "apple": "good for making cidar",
         "lemon": "a sour yellow citrus fruit",
         "grape": "a small sweet fruit growing in branches",
         "lime": "a sour,green fruit",
         "apple": "Round and crunchy"}

print(fruit)
print(fruit["lemon"])

motorbike = {"make": "honda", "model": "250dream", "color": "Red", "Engine": "250"}
print(motorbike["color"])
fruit["pear"] = "odd shaped apple"
print(fruit)
# sorted(fruit)
print(fruit)
del fruit["apple"]
print(fruit)
# fruit.clear()
print(fruit)
# while True:
#     dict_1 = input("Enter the values: ")
#     if dict_1 == "quit":
#         break
#     print(fruit.get(dict_1, "We dont have "+dict_1))
for i in range(10):
    for snack in fruit:
        print(fruit[snack])
    print("="*50)
print("*+="*40)
ordered_keys = list(fruit.keys())
ordered_keys.sort()
for keys1 in ordered_keys:
    print(fruit[keys1])

print("*+="*40)
for x in fruit:
    print(fruit[x])
print(list(fruit.values()))
print(fruit.values())

f_tupl = tuple(fruit.values())
print(f_tupl)

f_tupl = tuple(fruit.items())
print(f_tupl)
print(dict(f_tupl))
s = "Alpit"
for i in range(10):
    s = s+'A'

print(s)
