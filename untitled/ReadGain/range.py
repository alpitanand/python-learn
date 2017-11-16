print(range(100))
print(range(-10))
print(range(-0))
# print(range(.01))
my_list = list(range(10))
print(my_list)
my_list = list(range(-10, -1))
print(my_list)
even = list(range(0, 10, 2))
print(even)
my_string = "abcdefghijklmnopqrstuvwxyz"
print(my_string.index('e'))
print(my_string[4])
small_deci = range(0, 100, 2)
print(small_deci)
print(small_deci[4])
div_seven = range(7, 100000000, 7)
# x = int(input("Enter the number divisible by seven: "))
# if x in div_seven:
#     print(div_seven.index(x)+1)
decimal = range(0, 100)
rang = decimal[3:40:3]
print(rang == range(3, 40, 3))
print("="*10)
r = range(1, 100, -3)
for i in r[::2]:
    print(i)

