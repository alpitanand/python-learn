import requests
res=requests.get('http://inventwithpython.com/page_that_does_not_exist')
try:
    res.raise_for_status()
except Exception as al:
    print('Error downloading')
type(res)
t=len(res.text)
helofile =open('D:\\alpit1\\a1.txt','w')
helofile.write(res.text[0:])