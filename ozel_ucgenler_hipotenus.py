# Soru: [3, 4, 5, 12, 6, 8, 7, 24] listesindeki ikili dik kenarları ayırıp hipotenüslerini hesaplayınız.
# Burada listeyi 2'şerli adımlarla gezip her (a, b) çifti için Pisagor ile hipotenüsü bulduk.

kenarlar = [3, 4, 5, 12, 6, 8, 7, 24]

for i in range(0, len(kenarlar), 2):
    a = kenarlar[i]
    b = kenarlar[i + 1]
    c = (a**2 + b**2) ** 0.5
    print(f"Kenarlar: ({a}, {b}) -> Hipotenüs: {c:.1f}")
