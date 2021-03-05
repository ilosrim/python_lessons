# cars = {
#     'model':'ferrari',
#     'rang':'qizil'
#     }
# print(cars['model'])
# print(cars['rang'])

# talaba = {
#     'ism':'hasan husanov',
#     'yosh':20,
#     't_yil':'2005'
#     }
    
# talaba['kurs'] = 3
# talaba['fakultet'] = 'biologiya'
# talaba['kurs'] = 4
# print(f"{talaba['ism'].title()} {talaba['t_yil']}-yilda tug'ilgan, {talaba['yosh']} yoshda. {talaba['kurs']}-kursda o'qiydi.")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar['hasan']
phone = telefonlar.get('hasan','Bunday ism mavjud emas!')
print(f"Alining telefoni {phone}")