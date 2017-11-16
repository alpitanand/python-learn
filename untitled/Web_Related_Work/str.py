str1 = "Alpit is a great guy"
letter=str1[0]
length=len(str1)
print(letter)
print(length)
index=0
while index<length:
    print(str1[index])
    index+=1
print(str1.find("is"))
print(str1.startswith("Alpit"))

camels=42
print("I have spotted %d camels" % camels)

