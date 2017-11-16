_author_ = 'dev'
name = input("Enter your name: ")
age = int(input("What is your age {0}: ".format(name)))
print(age)
if age >= 18:
    print('Old enough to vote')
else:
    print("Please come back in {} year".format(18-age))


