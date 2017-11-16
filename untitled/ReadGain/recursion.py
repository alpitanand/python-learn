a = int(input("Enter a number \n"))
b = 1
for i in range(1, a+1):
    b *= i
print(b)


def fact(n):
    if n == 1:
        return 1
    else:
        return n*fact(n-1)


def fibonacci(n):
    t = 0
    h = 1
    print(t)
    print(h)
    for i in range(0, 5):
        m = t+h
        print(m)
        t = h
        h = m


def recur_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return recur_fibonacci(n-1)+recur_fibonacci(n-2)


print(fact(5))
# fibonacci(5)
print(recur_fibonacci(10))
