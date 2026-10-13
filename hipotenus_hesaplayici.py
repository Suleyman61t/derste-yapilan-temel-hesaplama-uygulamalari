# Soru: İki dik kenarı girilen dik üçgenin hipotenüs uzunluğunu hesaplayınız.
# Burada kullanıcıdan a ve b kenarlarını alıp Pisagor bağıntısıyla (c = (a**2 + b**2)**0.5) hipotenüsü bulduk.

a = float(input("1. Dik Kenar (a): "))
b = float(input("2. Dik Kenar (b): "))

c = (a**2 + b**2) ** 0.5

print("Hipotenüs:", c)
