# yosh = int(input("Yoshingizni kiriting: "))
# if yosh<=4:price=0 # yosh bolalarga bepul
# elif yosh<=12:price=5000 # 4 dan 12 yoshgacha 5000 so'm
# elif yosh<65:price=10000 # 12 dan katta va 65 dan kichiklarga 10000 so'm
# elif yosh>=65:price=8000 # qariyalarga 8000 so'm
# print(f"Sizga kirish {price} so'm")

# kun = input("Bugun qanday kun? \n>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni.")
# else:
#     print("Bugun ish kuni.")

#menu = ['osh', 'qazonkabob', 'shashlik', 'norin', 'somsa']
# print('osh' in menu )# menu da osh bormi?

# ovqat = input("Nima ovqat buyurasiz?\n>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo'q")

# buyurtmalar = ["osh", "somsa", "shashlik", "manti"]
# if buyurtmalar:
#     for taom in buyurtmalar:
#         if taom in menu:print(f"Menuda {taom} bor")
#         else:print(f"Menuda {taom} yo'q")
# else:print("Savatchangiz bo'sh")


#VAZIFA

#1
son = int(input("Juft son kiriting: "))
if son%2==0: print("Rahmat")
else: print("Son juft emas")

#2
yosh = int(input("Yoshingizni kiriting: "))
if yosh<=4 or yosh>=60:narx=0
elif yosh<=18:narx=10000
elif yosh>18:narx=20000
print(f"Chipta narhi {narx} so'm")

#3
mahsulotlar = ["anor", "anjir", "o'rik", "shaftoli", "olma", "gilos", "olcha", "olxo'ri", "bodom","yeryong'oq", "yong'oq"]
savat = []
for n in range(5):
    savat.append(input(f"{n+1}-mahsulotni qo'shing: "))
bor_mahsulotlar = []
mavjud_emas = []
for mahsulot in savat:
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else:
        mavjud_emas.append(mahsulot)

if mavjud_emas:
    print(f"Do'konimizda quyidagi maxsulotlar yo'q:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
else:
    print("Siz so'ragan barcha maxsulotlar do'konimizda bor.")