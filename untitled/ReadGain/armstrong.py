a = int(input())
b = a
t = 0
while a > 0:
    c = a % 10
    t += c ** 3
    a //= 10
print(t)
if t == b:
    print("Armstrong")
else:
    print("Not armstrong")


