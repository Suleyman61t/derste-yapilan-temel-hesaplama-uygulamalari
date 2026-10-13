# Soru: range(1, 11) ile 1D NumPy dizisi oluşturup hem döngüyle hem de vektörel olarak elemanların karesini alınız.
# Burada range ile dizi oluşturup for döngüsü ve dizi**2 vektörel işlemiyle karelerini hesapladık.

import numpy as np

# range ile 1'den 10'a dizi
dizi = np.array(range(1, 11))
print("Orijinal dizi:", dizi)

# 1) Döngü ile kare alma
kareler_dongu = []
for sayi in dizi:
    kareler_dongu.append(sayi ** 2)
print("Döngü ile kareler:", kareler_dongu)

# 2) NumPy vektörel işlemle kare alma
kareler_vektorel = dizi ** 2
print("Vektörel kareler :", kareler_vektorel)
