import random
print(dir())
for x in dir(__builtins__):
    print(x)

for i in range(1, 20):
    print(random.randint(0, 20))
