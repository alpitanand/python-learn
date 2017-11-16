fhand=open('run.txt')
print(fhand)
count=0
coun2=0
pong = 'hello\nworld'
print(pong)
for line in fhand:
    line=line.rstrip();
    count+=1
    coun2=coun2+len(line)
    if line.startswith("From"):
        print(line)
    if not line.startswith("From"):
        continue
print(count)
print(coun2)
