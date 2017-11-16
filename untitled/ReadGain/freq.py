a = 'Alpit is a a  a a aa a a a a a a a great guy'
m = a.split()
t = {}
for w in m:
    if w in t:
        t[w] += 1
    else:
        t[w] = 1
print(t)



