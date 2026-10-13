# Soru: 100 rastgele tam sayıdan 10x10 matris oluşturup ilk ve son satırını çarpınız; matrisin en büyük, en küçük ve standart sapma değerlerini bulunuz.
# Burada np.random.randint(1, 1000, 100) ile 100 rastgele sayı üretip reshape(10, 10) yaptık, satırları çarptık ve max(), min(), std() hesapladık.

import numpy as np

# 100 rastgele sayıdan 10x10 matris (1 ile 1000 arası rastgele tam sayılar)
dizi = np.random.randint(1, 1000, 100)
matris = dizi.reshape(10, 10)

ilk_satir = matris[0]
son_satir = matris[-1]
carpim = ilk_satir * son_satir
toplam = carpim.sum()

en_buyuk = matris.max()
en_kucuk = matris.min()
standart_sapma = matris.std()

print("10x10 Rastgele Matris:\n", matris)
print("\nİlk Satır:\n", ilk_satir)
print("\nSon Satır:\n", son_satir)
print("\nÇarpım Sonucu (Eleman Bazlı):\n", carpim)
print("\nÇarpım Elemanlarının Toplamı:", toplam)
print("\nMatris En Büyük Değer :", en_buyuk)
print("Matris En Küçük Değer :", en_kucuk)
print(f"Matris Standart Sapma : {standart_sapma:.2f}")
