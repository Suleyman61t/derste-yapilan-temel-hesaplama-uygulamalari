# Soru: 15. Bilimsel Uygulama - Sabit İvmeli Hareket (Sayfa 8)
# x(t) = v0*t + 1/2*a*t^2 formülü ile 0-10 saniye arası her x konum değerini yazdırınız.
# Burada t=10'a kadar 0.5 adımlarla zaman dizisi oluşturup her an için konumu tek tek yazdırdık.

import numpy as np

v0 = 10
a = 2
t = np.arange(0, 10.5, 0.5)
x = v0 * t + 0.5 * a * (t ** 2)

for i in range(len(t)):
    print(f"t = {t[i]:4.1f} s -> x = {x[i]:6.2f} m")
