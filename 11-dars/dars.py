"""ITEMS FUNCTION"""
talaba_0 = {
    'ism':'alijon',
    'familiya':'shamshiyev',
    'yosh':22,
    'fakultet':'matematika',
    'kurs':4
    }

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit: {kalit}")
#     print(f"Qiymat: {qiymat} \n")

###

phons = {
    'ali':'iphone x',
    'vali':'galaxy j6',
    'hasan':'motorolla',
    'husan':'nokia',
    'eshmat':'galaxy j6',
    'toshmat':'iphone x'
}

# for k, q in phons.items():
#     print(f"{k.title()}ning telefoni {q.title()}")
"""KEYS FUNCTION"""
# talaba_0 = {
#     'ism':'alijon',
#     'familiya':'shamshiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
#keys.() funksiasini for da ishlatmasak ham natija chiqadi
#for kalit in talaba_0.keys():
    #print(f"Kalit: {kalit}")

###

mahsulotlar = {
    'olma':10000,
    'anor':20000,
    'uzum':40000,
    'anjir':25000,
    'shaftoli':30000
    }
bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling!")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# print(talaba_0.values())
#print("Foydalanuvchi quyidagi telefonlarni ishlatadi:")
#for tel in set(phons.values()): #set() qaytalanishni oldini oladi
    #print(tel.title())

"""VAZIFA"""
#item(), keys(), values()
#1
py_lugat = {
    'integer':'butun son',
    'float':'o\'nlik son',
    'string':'matn',
    'boolean':'mantiqiy operator',
    'for':'amalni qayta bajarish',
    'if':'shartlarni tekshirish',
    'def':'funksiya',
    'list':'ro\'yxat',
    'tuple':'o\'zgarmas ro\'yxat',
    'dictionary':'lug\'at'
}
for k, q in sorted(py_lugat.items()):
    print(f"{k.title()} - {q}")

davlatlar = {
    'o\'zbekiston':'toshkent',
    'qirg\'izizson':'bishkek',
    'qozog\'iston':'nursulton',
    'turkiya':'anqara',
    'italiya':'rim',
    'fransiya':'parij',
    'buyuk britaniya':'london',
    'aqsh':'washington d.c',
    'singapur':'singapur',
    'malayziya':'kuala-lumpur'
}

print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
    print(davlat.upper())

print("Davlatlarning poytaxtlari:")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

country = input("Qaysi davlatning poytaxtini bilishni istaysiz?: ").lower()
capital = davlatlar.get(country)
if capital==None:
    print("Kechirasiz, bizda bunday malumot yo'q")
else:
    print(f"{country.upper()} ning poytaxti {capital.title()} shahri.")

menu = {
    'osh':15000,
    'manti':10000,
    'somsa':5000,
    'sho\'rva':7000,
    'kavob':5000,
    'lavash':17000,
    'gumma':1500,
    'burger':7500
}
print("3 ta taom buyurtma bering!")
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in menu:
        print(f"{buyurtma.title()} {menu[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, {buyurtma} menu da yo'q!")