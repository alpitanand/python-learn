elements1 = {}


def python_food():
    width = 80
    length = len("Spam and eggs")
    diff = (width - length) // 2
    print("Spam and eggs")
    print(diff)


def center_text(text):
    print('Print anything')
    print(text)


def add(number):
    list1 = []
    for k in range(0, number):
        list1.append(k)
    print(list1)


def frequency(num):
    if num in elements1.keys():
        elements1[num] = elements1.get(num)+1
    elif num not in elements1.keys():
        elements1[num] = 1


def mul_parameter(*args):
    text = ''
    for arg in args:
        text += str(arg)+""
    with open('Alpit.txt', 'w') as alpit:
        print(text, file=alpit)


python_food()
center_text('Hello world')
center_text("he is a nice boy")
add(10)
mul_parameter('alpit', 12, 23, 'Prachee')
