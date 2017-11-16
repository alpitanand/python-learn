# list = input("Enter the ip address: ")
# b = list.count('.')
# print(b)

parrot_list = ["dead", "alive", "running", "hopping"]
for state in parrot_list:
    print("Parrot is {}".format(state))
print("=============================")
parrot_list.append("Bird")
for state in parrot_list:
    print("Parrot is {}".format(state))

even = [2, 4, 6, 8, 10]
odd = [1, 3, 5, 7, 9]
number = even+odd
print(number)
number.sort()
# here number sort is directly changing the list without creating a new object
print(number)
print(sorted(number))
if number == even:
    print("Equal")
else:
    print("Nt equal")

