# Soru: 100 elemanlı dizi oluşturup 10x10 matrise çeviriniz ve ilk satır ile son satırı çarpınız.
# Burada np.arange ile 1-100 arası dizi oluşturup reshape(10, 10) yaptık ve matris[0] ile matris[-1] satırlarını çarptık.

import numpy as np

# 100 elemanlı dizi ve 10x10 matris
dizi = np.arange(1, 101)
matris = dizi.reshape(10, 10)

ilk_satir = matris[0]
son_satir = matris[-1]
carpim = ilk_satir * son_satir

print("İlk Satır:\n", ilk_satir)
print("\nSon Satır:\n", son_satir)
print("\nÇarpım Sonucu (Eleman Bazlı):\n", carpim)
