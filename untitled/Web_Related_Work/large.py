largest = 0
small=9999
numbers = [1, 2, 3, 5, 34, 54, 34, 12, 53, 232, 32, 24, 24]
numbers2 = [1, 2, 3, 5, 34, 54, 34, 12, 53, 232, 32, 24, 24]
for number, number1 in numbers,numbers2:
    if number > largest:
        largest = number
    if number1 < small:
        small=number1
print(largest)
print(small)
