# matn = "Kayfiyatlar qalay 🤪"
# print(matn)

# ism = "Sher"
# print("Mening ismim " + ism)

# ism = "Ahad"
# familya = "Qayum"
# print(ism + ' ' + familya)

# ism = "Ahad"
# familya = "Qayum"
# ism_sharif = f"{ism} {familya}"
# print(ism_sharif)
# print(f"Salom, mening ismim {ism}. {ism} {familya}")

# sher = "Izlarsan o'tmishingdan ziyo, \nIzsiz ketkan bo'lsangda..."
# print(sher)

# ism = input("Ismingizni kiriting:\n")
# print("Salom " + ism.title() + ", saytimizga hush kelibsiz!")

# xabar = input("O'zingiz haqingizda ma'lumot bering:\n")
# print(xabar.capitalize())

#VAZIFA
# kocha = "Bog'bon"
# mahalla = "Sog'bon"
# tuman = "Bodomzor"
# viloyat = "Samarqand"
# print(
#           kocha + " ko'chasi, "
#         + mahalla + " mahallasi, "
#         + tuman + " tumani, "
#         + viloyat + " viloyati.")

# kocha = input("Ko'chani kiriting:\n")
# mahalla = input("Mahallani kiriting:\n")
# tuman = input("Tumanni kiriting:\n")
# viloyat = input("Viloyatni kiriting:\n")
# manzil = f"{kocha}, {mahalla}, {tuman}, {viloyat}."
# print(manzil.title())

#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ").title()
mahalla = input("Mahallangiz: ").title()
tuman = input("Tumaningiz: ").title()
viloyat = input("Viloyatingiz: ").title()
print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + \
      tuman + " tumani, " + viloyat + " viloyati") 