# Soru: 100 elemanlı dizi oluşturup 10x10 matrise çeviriniz, ilk ve son satırı çarpıp çarpım dizisinin toplamını bulunuz.
# Burada reshape(10, 10) yapıp ilk ve son satırı çarptık ve çarpım dizisinin toplamını (carpim.sum()) hesapladık.

import numpy as np

# 100 elemanlı dizi ve 10x10 matris
dizi = np.arange(1, 101)
matris = dizi.reshape(10, 10)

ilk_satir = matris[0]
son_satir = matris[-1]
carpim = ilk_satir * son_satir
toplam = carpim.sum()

print("İlk Satır:\n", ilk_satir)
print("\nSon Satır:\n", son_satir)
print("\nÇarpım Sonucu (Eleman Bazlı):\n", carpim)
print("\nÇarpım Elemanlarının Toplamı:", toplam)
