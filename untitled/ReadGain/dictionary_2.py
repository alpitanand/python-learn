alfa = ["a", "b", "c", "d"]
newstr = ''
for i in alfa:
    newstr += i +","
print(newstr)
print(",".join(alfa))
letter = 'abcdefghijklmnopqrstuvwxyz'
info = 'abcd'
print(",".join(letter))
print(list(letter))
print(tuple(list(letter)))
print(tuple(letter))
k = tuple(info)
print(k)
qw, b, c, d = k
print(qw)

number = '1234567890'
print(" missippi, ".join(number))
