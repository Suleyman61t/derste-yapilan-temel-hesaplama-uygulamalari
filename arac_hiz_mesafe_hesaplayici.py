# Soru: 90 km/s sabit hızla giden aracın verilen dakikada aldığı yolu hesaplayınız.
# Burada kullanıcının girdiği dakikayı saate çevirip x = v * t ile yolu bulduk.

hiz = 90.0
dakika = float(input("Dakika giriniz: "))

saat = dakika / 60.0
yol = hiz * saat

print("Alınan yol (km):", yol)
