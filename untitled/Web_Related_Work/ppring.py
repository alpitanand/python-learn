import pprint
s="This is a nyc sunny day and birds are chirping"
count={}
for a in s:
    count.setdefault(a,0)
    count[a]=count[a]+1

for b in s.split("and"):
    print(b)
pprint.pprint(count)