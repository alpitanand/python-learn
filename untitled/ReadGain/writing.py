cities = ["Patna", "BBSr", "Ranchi", "Jharkhand", "Puriii",'gaya']
with open("cities.txt", 'r') as city_file:
    # for city in cities:
    #     print(city, file=city_file)
    sen = city_file.readlines()
    print(sen)


# alpit = open("city2.txt", 'a')
# for line in cities:
#     print(line, file=alpit)
# for a in range(2, 13):
#     for b in range(1, 11):
#         print("{} times {} = {}".format(a, b, a*b), file=alpit)
#     print("-"*20,file=alpit)
#
#
# alpit.close()
#
# print("abrakadabraw".strip('abra'))
#
# imelada = "Alpit", "is", "great", (("1", "heya"), ("2", "lolwa"))
# print(type(imelada))
