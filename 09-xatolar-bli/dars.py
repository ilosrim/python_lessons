# """xatoliklar bo'yicha amallar"""
# son = float(input("Istalgan son kiriting: "))
# if son%2!=0:
#     print("Bu son juft emas!")
# else:
#     print("Rahmat!")

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz','kartoshka','olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:print(f"Do'konimizda {mahsulot} bor")
#         else:print(f"Do'konimizda {mahsulot} yo'q")
# else:print("Savatingiz bo'sh")

# ####

# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#                'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#   print("Do'konimizda quyidagi mahsulotlar yo'q:")
#   for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

# users = ['alisher1983','aziza','yasina', 'umar']

# login = input("Yangi login tanlang: ")

# if login.lower() in users:
#     print('Login band, yangi login tanalng!')
# else:
#     print(f"Xush kelibsiz {login.title()}!")

age = 7
print(f"Tommy is {age}, years old")
