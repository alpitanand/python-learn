birthday = {"ALpit": "24 Aug", "Prachee": "13 May", "Arshita": "29 Feb"}
list = ("ALpit", "Prachee", "Priyanshi", "MAdhu")
name = "ALpit"
if name in birthday:
    print(birthday[name] + "is the birthday of" + name)
elif name not in birthday:
    s = input("Ï dont have bday info,ENter bday")
    birthday[name] = s
    print("Data base updated")
for name in birthday:
    print(birthday[name] + " is the bday of " + name)
for i in list:
    print(i, end='')
print("\nI have  "+str(birthday.get("Priya","Hurre"))+" hcag ")
print("yeha")