import datetime

# avtolar = ['audi','bmw','volvo','kia','hyundai']
# for avto in avtolar:
#     if avto == "bmw":
#         print(avto.upper())
#     else:
#         print(avto.title())

# ism = input("Ismingizni kiriting: \n>>")
# if ism.lower() != 'ali':
#     print(f"Uzur {ism.title()}, biz Alini kutayapmiz!")
# else:
#     print("Salom Ali!")

# yosh = int(input("Yoshingiz nechada?\n>>"))
# if yosh >=18:
#     print('Hush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')

# login = input("Yangi login kiriting:\n>>")
# if len(login)<8:
#     print("Login 8 tadan ko'p bo'lishi shart!")
# else:
#     print("OK")

# x = datetime.datetime.now()
# yil = int(input("Tug'ulgan yilingizni kiriting: \n>>"))
# if int(x.strftime("%Y"))-yil<18:
#     print(f"Sizning yoshingiz {int(x.strftime('%Y'))-yil} da ekan.")
#     print("Kirish mumkin emas!")
# else:
#     print("Hush kelibsiz")

#VAZIFA

#1
cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for car in cars:
    if car != 'gm':
        print(car.title())
    else:
        print(car.upper())

#2
login = input("Login kiriting: ")
if login.lower() == 'admin':
    print("Salom Admin")
else:
    print(f"Hush kelibsiz {login.title()}!")

#3
print("Istalgan ikki son kiriting:")
son1 = float(input("1-son: "))
son2 = float(input("2-son: "))
if son1 == son2:
    print("Sonlar teng")
elif son1 > son2:
    print("1-son katta")
else:
    print("2-son katta")