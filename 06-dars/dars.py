# mehmonlar = ['Ali', 'Vali', 'Ahad', 'Qayum']
# for mehmon in mehmonlar:
#     print(mehmon)

# sonlar = list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng.")

# numbers = list(range(11))
# numKv = []
# for num in numbers:
#     numKv.append(num**2)
# print(numbers)
# print(numKv)

# friends = []
# print('5 ta istalgan do\'stingiz kim ?')
# for n in range(5):
#     friends.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
# print(friends)

#VAZIFA
#1
ismlar = ["Hasan", "Husan", "Ahad", "Qayum", "Eshmat", "Toshmat"]
for ism in ismlar:
    print(f"Salom {ism}!")
print(f"Kod {len(ismlar)} marta takrorlandi.")
#for n in range(10,101):
    #print(n**3)

#2
kinolar = []
print("5 ta yoqtirgan kino nomini yozing: ")
for n in range(5):
    kinolar.append(input(f"{n+1}-kino nomi: "))
print(kinolar)

#3
suhbatdoshlar = []
print("Bugun nechta odeam bilan suhbat qurdingiz?")
for n in range(3):
    suhbatdoshlar.append(input(f"{n+1}-suhbatdosh: "))
print(suhbatdoshlar)
print(f"Umumiy suhbat doshlar soni: {len(suhbatdoshlar)}")