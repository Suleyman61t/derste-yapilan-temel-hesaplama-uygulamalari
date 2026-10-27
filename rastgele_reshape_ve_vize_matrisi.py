# Soru: 1) Rastgele bir dizi oluşturup reshape ile farklı boyutta matrise dönüştürünüz. 2) 70 üzeri notlardan oluşan bir vize matrisi tanımlayıp genel ortalamasını hesaplayınız.
# Burada np.random ile üretilen diziyi reshape ettik ve 70 üzeri değerler içeren vize matrisinin np.mean() ile ortalamasını aldık.

import numpy as np

# Uygulama 1: Rastgele dizi oluşturma ve reshape
rastgele_dizi = np.random.randint(1, 100, 12)
matris_3x4 = rastgele_dizi.reshape(3, 4)

print("Uygulama 1 - Orijinal 1D Dizi:\n", rastgele_dizi)
print("\nUygulama 1 - 3x4 Matris (Reshape):\n", matris_3x4)

# Uygulama 2: 70 üstü vize matrisi ve ortalaması
vize_notlari = np.array([
    [75, 82, 90],
    [88, 72, 95],
    [78, 85, 92]
])

genel_ortalama = np.mean(vize_notlari)

print("\n" + "=" * 40)
print("Uygulama 2 - Vize Notları Matrisi:\n", vize_notlari)
print(f"\nVize Notları Genel Ortalaması: {genel_ortalama:.2f}")
