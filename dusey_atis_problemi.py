# Soru: 120m yükseklikten 5 m/s ilk hızla aşağı atılan cismin 3 saniye sonraki konumunu ve hızını bulunuz.
# Burada düşey atış formülleriyle (h = v0*t + 0.5*g*t^2) düşülen yolu, kalan yüksekliği ve anlık hızı bulduk.

h0 = 120.0
v0 = 5.0
g = 10.0
t = 3.0

dusulen_yol = (v0 * t) + (0.5 * g * (t ** 2))
kalan_yukseklik = h0 - dusulen_yol
hiz = v0 + (g * t)

print("Alınan yol (m):", dusulen_yol)
print("Yerden yükseklik (m):", kalan_yukseklik)
print("Anlık hız (m/s):", hiz)
