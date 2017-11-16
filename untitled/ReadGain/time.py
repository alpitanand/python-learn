import time
print(time.gmtime(0))
print(time.localtime(time.time()))
time_here = time.localtime()
print('Year:', time_here[0], time_here.tm_year)
print('Year:', time_here[1], time_here.tm_hour)
