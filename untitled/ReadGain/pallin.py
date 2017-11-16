c = 0
str = input("Enter a string")
for i in range(len(str)):
    if str[i] == str[-i]:
        c += 1
if c == len(str):
    print("palindrome")
else:
    print("Not a palindrome")

