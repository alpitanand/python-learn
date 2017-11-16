number = "9,323,23,22,232,132,323"
cleannumber = ''
for char in number:
    if char in '0123456789':
        cleannumber += char
print(int(cleannumber))

for state in ['alive', 'dead', 'speaking', 'running', 'walking']:
    print("Alpit is {}".format(state))

for i in range(0, 100, 5):
    print("i is {}".format(i))

for i in range(0, 11):
    for j in range(0, 11):
        print("{0} is to {1} is {2}".format(i, j, (i*j)))
    print('===================')

