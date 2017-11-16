class Service(object):
    data = []
    class_var = 1

    def __init__(self, other_data):
        self.other_data = other_data


s1 = Service(['a', 'b'])
s2 = Service(['c', 'd'])
print(s1.other_data)
print(s2.other_data)
print(s1.data)
s1.data.append(1)
print(s1.data)
print(s2.data)
print(Service.data)
s1.class_var = 2
print(Service.class_var)
print(s1.class_var)

a = "Alpit \nis a real\t\tly nice boy"
print(a)
c = '1000 Maniacs	Our Time in Eden	1992	Candy Everybody Wants'
print(c.split('\t'))

