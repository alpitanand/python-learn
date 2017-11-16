#birthday={'Alpit':'24 Aug','Arshita':'1 March','Prachee':'13 March'}
# name= input();
# if name in birthday:
#     print(birthday[name]+" is the bithday of "+ name)
# else:
#     print("No name found,enter the bday")
#     bday=input();
#     birthday[name]=bday
# for m in birthday.keys():
#     print(m)
#print("birthday is "+ str(birthday.get('Alpit',0)))
message="My name is alpit and i am a very great guy"
count={}
for i in message:
    count.setdefault(i,0)
    count[i]=count[i]+1
print(count)

spam={'name': 'Pooka', 'age': 5}
spam.setdefault('Color','black')
print(spam)
spam['Color']='white'
print(spam)