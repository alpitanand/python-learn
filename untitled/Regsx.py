# import re
# message='Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
# phnoRegx=re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
# mo=phnoRegx.search(message)
# print("Phone numbers "+mo.group())

import re
bat="I am a batwowowowoman and batman"
regx=re.compile(r'bat(wo)*man')
mo2=regx.search(bat)
print(mo2.group()+" "+mo2.group(1))

mes="i am a great guy"
reg1=re.compile(r'[^aeiou]')
m=reg1.findall(mes)
print(m)