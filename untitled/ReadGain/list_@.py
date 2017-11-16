list_1 = []
list_2 = list()
if list_1 == list_2:
    print("Equals")
print(list("The list is equal"))

even = [2, 4, 6, 8]
another_even = even
another_even.sort(reverse=True)
# even is sorted because another_even and even both refer to same list
print(even)
# by using this we can create an entirely new object of list for reference
another_even = list(even)

odd = [1, 3, 5, 7, 9]
number = [even, odd]
print(number)
for number_set in number:
    for value in number_set:
        print(value)

