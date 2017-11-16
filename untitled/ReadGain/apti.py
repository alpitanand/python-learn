t = 0
for i in range(1, 1001):
    if 1000 % i == 0:
        print(i)
        t += 1
print("The number of divisors {}".format(t-1))
