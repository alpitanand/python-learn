import re
nameReg = re.compile(r'alpit(anand|prachee)')
mo = nameReg.findall('alpitanand')
print(mo)


