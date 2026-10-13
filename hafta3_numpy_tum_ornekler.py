# Soru: 3. Hafta NumPy slaytındaki temel dizi oluşturma, linspace ve matris dilimleme örneklerini uygulayınız.
# Burada np.arange, np.linspace ve 3x3 matris dilimleme (slicing) işlemlerini yaptık.

import numpy as np

# 1) 0-100 arası 5'erli dizi
dizi1 = np.arange(0, 101, 5)
print("0-100 arası 5'erli dizi:\n", dizi1)

# 2) 1-20 arasında 20 eşit aralıklı değer
dizi2 = np.linspace(1, 20, 20)
print("\n1-20 arası 20 eşit nokta:\n", dizi2)

# 3) 3x3 matris ve dilimleme
A = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])
print("\nMatris A:\n", A)
print("1. satır:", A[0, :])
print("2. sütun:", A[:, 1])
print("Merkez eleman:", A[1, 1])
