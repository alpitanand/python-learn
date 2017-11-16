# jabber = open("C:\\Users\\RakeshS\\Desktop\\sample.txt", 'r')
# for line in jabber:
#     print(line, end='')
# jabber.close()

with open("C:\\Users\\RakeshS\\Desktop\\sample.txt", 'r') as jabber:
    line = jabber.readline()
    while line:
        print(line, end='')
        line = jabber.readline()

print("=="*40)

with open("C:\\Users\\RakeshS\\Desktop\\sample.txt", 'r') as jabber:
    lines = jabber.readlines()
print(lines)
for line in lines[::-1]:
    print(line, end='')

print("=="*40)

with open("C:\\Users\\RakeshS\\Desktop\\sample.txt", 'r') as jabber:
    lines = jabber.read()
print(lines)
for line in lines[::-1]:
    print(line, end='')

