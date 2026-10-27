# Soru: 7. Hafta Sayfa 11 - Denklem sisteminin katsayılar (A) ve sonuç (R) matrislerini oluşturup, A'nın tersi ile R'yi çarparak x, y, z değerlerini bulunuz.
# 2x - 3y + z = 1
# 5x - 4y - z = 2
# x + 2z = -1
# Burada np.linalg.inv(A) ile katsayılar matrisinin tersini alıp R ile matris çarpımı (@) yaparak x, y, z köklerini bulduk.

import numpy as np

# Katsayılar matrisi (A) ve Sonuç matrisi (R)
A = np.array([
    [2, -3,  1],
    [5, -4, -1],
    [1,  0,  2]
], dtype=float)

R = np.array([
    [1],
    [2],
    [-1]
], dtype=float)

# A'nın tersini alma ve R ile çarpma: X = A^(-1) @ R
A_ters = np.linalg.inv(A)
cozum = A_ters @ R

x = cozum[0, 0]
y = cozum[1, 0]
z = cozum[2, 0]

print("Katsayılar Matrisi (A):\n", A)
print("\nSonuç Matrisi (R):\n", R)
print("\nA'nın Tersi (A^-1):\n", A_ters)
print("\nÇözüm Matrisi (X = A^-1 @ R):\n", cozum)
print("-" * 35)
print(f"x = {x:.4f}")
print(f"y = {y:.4f}")
print(f"z = {z:.4f}")
