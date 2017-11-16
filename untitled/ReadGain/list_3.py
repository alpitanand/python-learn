# on iterator
string = '1234567890'
for char in string:
    print(char)
print("=================")
for char in iter(string):
    print(char)

my_iter = iter(string)
print("=================")
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
print(next(my_iter))
# print(next(my_iter))

liste = list(string)
print(liste)
itre = iter(liste)
for i in range(len(liste)):
    print(next(itre))


