# Soru: 3x3 bir matrisin elemanlarını matris düzeninde ekrana yazdırıp genel toplamını bulunuz.
# Burada iç içe döngü kullanarak 3x3 matrisi satır satır yazdırdık ve elemanları topladık.

matris = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

toplam = 0

print("Matris:")
for satir in matris:
    for eleman in satir:
        print(eleman, end=" ")
        toplam += eleman
    print()

print("\nElemanların Toplamı:", toplam)
