import pickle

# imelda = ('More mayhem',
#           'Imelda may',
#           '2011',
#           ((1, 'Patna'),
#            (2, 'Bbsr'),
#            (3, 'Gaya')))
# with open('imelda.pickle', 'wb') as pickle_file:
#     pickle.dump(imelda, pickle_file)

# with open('imelda.pickle', 'rb') as imelda_pickle:
#     imelda2 = pickle.load(imelda_pickle)
# print(imelda2)

imelda = ('More mayhem',
          'Imelda may',
          '2011',
          ((1, 'Patna'),
           (2, 'Bbsr'),
           (3, 'Gaya')))
odd = list(range(0, 10, 2))
even = list(range(1, 10, 2))

with open('imelda.pickle', 'wb') as pickle_file:
    pickle.dump(imelda, pickle_file)
    pickle.dump(odd, pickle_file)
    pickle.dump(even, pickle_file)
    pickle.dump(121323123123123, pickle_file)

with open('imelda.pickle', 'rb') as imelda_pickle:
    imelda2 = pickle.load(imelda_pickle)
    even = pickle.load(imelda_pickle)
    odd = pickle.load(imelda_pickle)
    x = pickle.load(imelda_pickle)

print(imelda2)
print(even)
print(odd)
print(x)
