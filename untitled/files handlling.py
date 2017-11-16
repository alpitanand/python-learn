import os
t=os.path.join('usr','bin','hmm')
print(t)
#current working directory
m=os.getcwd()
print(m)
#os.makedirs('D:\\alpit1')
helofile =open('D:\\alpit1\\a1.txt','a')
for i in range(10):
    helofile.write("My name is alpit anand\n")
content=helofile.read()
print(content)
helofile.close()
