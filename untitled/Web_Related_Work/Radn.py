import random

from Tools.scripts.treesync import raw_input


def lottery():
    for p in range(6):
        yield random.randint(1, 1000)


for num in lottery():
    print(num)

print(type(12.444444444444444444444444444444444444))
a = '100'
b = '200'
print(a + b)

c = raw_input("Enter the number")
print(c)
print("This is", int(c) + 2)
x = 10
y = 20
if x < y:
    print(x < y)
elif x > y:
    print(not (x > y))
print(max("hllalowwz"))
for i in range(1, 10):
    x = random.randint(2, 10)
    print(x)
