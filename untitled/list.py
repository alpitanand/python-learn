# alpit=['a',2,3,4,5,6,6,7];
# for i in range(len(alpit)):
#     print(alpit[i])

# alpit=[['a','b'],['c','d','f']]
# print(alpit[0:1])
# m=[1,2 ,3, 4, 5, 6]
# p=m+alpit
# print(p)
# del p[2]
# print(p)

# catnmame=[]
# while True:
#     print("Enter the cat name and nothing to end")
#     name=input()
#     if name=="":
#         break
#     else:
#         catnmame=catnmame+[name]
# for name in catnmame:
#     print(name)dg

# mypets =["alpit","anand","is","a"]
# name =input();
# if name not in mypets:
#     print("not there")
# else:
#     print("there")
# alpit ="name"
# alpit += " is alpt"
# print(alpit)
# a= mypets.index("alpit")
# print(a)
# mypets.append("great")
# print(mypets)

# a= [1,23,4,5,6,7,8]
# a.sort()
# n=a
# print(n)

# import random
#
# messgage=["i","am ","a","great","guy"]
# for i in range(100):
#     print(messgage[random.randint(0,len(messgage)-1)])
#
# egg =[1,2,34]
# egg=[4,5,6,7]
# print(egg)
import copy

a = [1, 2, 3, 4]
b = 1, 2, 3, 4
a.append(5)
c = copy.copy(a)
print(c)
c = copy.deepcopy(b)
print(c)
print(a)