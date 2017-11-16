import re
phnumberregx = re.compile(r"\d\d\d-(\d\d\d-\d\d\d\d)")
mo = phnumberregx.search("This is my phone number 977-826-080")
if mo.group() is None:
    print('No number found')
else:
    print(mo.group())
