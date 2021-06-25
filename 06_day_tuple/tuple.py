#Exercise level 1
brotha = ("Svartalheim", "Yazata", "Gboomers")
sista = ("Girlies", "Pokimen", "02")
siblings = brotha + sista
print(len(siblings))
x = list(siblings)
x.append("Emma") #Father
x.append("Isabella") #Mother\
family_members = tuple(x)
#unpack
# *siblings, parents= family_members
# print(siblings)
# print(parents)
#other way(the correct one IMO)
saudara = family_members[0:6]
ortu = family_members[6:]
print(saudara)
print(ortu)

fruits = ("Anggur", "apple", "Pisang")
vegetable = ("Onion", "Garlic", "Timun")
animal = ("Kuching", "Kuda", "Buaya")
food_stuff_tp = fruits + vegetable + animal
print(food_stuff_tp)
food_stuff_lt = list(food_stuff_tp)
middle = food_stuff_lt.pop((len(food_stuff_lt)-1)//2)
print(middle)
firstthree = food_stuff_lt[0:3]
lastthree = food_stuff_lt[5:9]
print(firstthree)
print(lastthree)
del food_stuff_tp

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')
print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)