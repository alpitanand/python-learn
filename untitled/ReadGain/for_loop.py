for i in range(1, 20):
    print(i)
j = 1
number = "9,786,897,878"
for i in range(0, len(number)):
    if number[i] in '0123456789':
        print(number[i], end='')
fact = int(input("the factorial"))
for i in range(1, fact+1):
    j = j*i
print(j)
