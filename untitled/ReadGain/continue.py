shopping_list = ['milk', 'pasta', 'bacon', 'pan', 'curd']
for item in shopping_list:
    if item == 'pasta':
        continue
    print(item)
print("================")

for item in shopping_list:
    if item == 'pasta':
        break
    print(item)
print(item)
print("================")

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
comman = []
for i in b:
    if i in a:
        comman.append(i)
print(comman)

