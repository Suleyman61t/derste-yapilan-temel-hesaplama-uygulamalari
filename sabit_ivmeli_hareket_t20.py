# Soru: 15. Bilimsel Uygulama - Sabit İvmeli Hareket (Sayfa 8)
# x(t) = v0*t + 1/2*a*t^2 formülü ile 0'dan 20 saniyeye kadar 0.5 adımlarla konumu hesaplayınız.
# Burada v0=10 m/s ve a=2 m/s^2 alarak t=np.arange(0, 20.5, 0.5) dizisiyle vektörel konum hesapladık.

import numpy as np

v0 = 10
a = 2
t = np.arange(0, 20.5, 0.5)  # 0-20 saniye arası (20 dahil)
x = v0 * t + 0.5 * a * (t ** 2)

print("Zaman (s):\n", t)
print("\nKonum (m):\n", x)
