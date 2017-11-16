import re
import pyperclip
text1=pyperclip.paste()
def extracter(text):
    reg1 = re.compile(r'(\d{3}|\(\d{3}\))?(\s|-|\.)?(\d{3})(\s|-|\.)(\d{4})')
    se1 = reg1.findall(text)
    ##print(se1)
    print("Phone number printed")
    print( )
    for i in range(len(se1)):
        print(''.join(se1[i]))
    reg2 = re.compile(r'([a-zA-Z0-9]+@+[a-zA-Z0-9]+\.[a-zA-Z]{2,4})')
    #reg3 = re.compile(r'(\w+)@')
    #se3 = reg3.findall(text)
    se2 = reg2.findall(text)
    print("Email id Printed:")
    print( )
    if not se2:
        print("Nothing is found")
    else:
        for r in range(len(se2)):
            print(''.join(se2[r]))

    #print(se3)
extracter(text1)
