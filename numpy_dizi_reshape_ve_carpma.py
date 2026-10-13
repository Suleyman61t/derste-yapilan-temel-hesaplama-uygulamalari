# Soru: 1-12 arası sayılardan oluşan bir diziyi (3, 4) şeklinde matrise dönüştürüp 3 ile çarpınız.
# Burada np.arange ile üretilen diziyi reshape(3, 4) yapıp skaler 3 ile çarparak matrisi güncelledik.

import numpy as np

# 1D dizi oluşturma
dizi = np.arange(1, 13)
print("1D dizi:\n", dizi)

# 3x4 matrise dönüştürme
matris = dizi.reshape(3, 4)
print("\n3x4 matris:\n", matris)

# 3 ile skaler çarpma
sonuc = matris * 3
print("\n3 ile çarpılmış matris:\n", sonuc)
