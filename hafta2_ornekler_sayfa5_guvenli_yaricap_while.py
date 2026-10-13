# Soru: Kullanıcı negatif yarıçap girdiği sürece tekrar isteyen ve doğru girilince alan/çevre hesaplayan programı yazınız.
# Burada while döngüsü ile negatif girişleri engelleyip pozitif değer gelince dairenin alan ve çevresini hesapladık.

import math

r = float(input("Yarıçapı giriniz: "))

while r < 0:
    print("Yarıçap negatif olamaz!")
    r = float(input("Tekrar giriniz: "))

alan = math.pi * (r ** 2)
cevre = 2 * math.pi * r

print("Dairenin Alanı:", round(alan, 2))
print("Dairenin Çevresi:", round(cevre, 2))
