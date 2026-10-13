# Soru: Kullanıcıdan alınan dizi elemanlarını 5 ile çarpıp yeni bir diziye aktarınız.
# Burada girilen elemanları listeye ekleyip her birini 5 ile çarparak yeni listeye yazdık.

adet = int(input("Eleman sayısı: "))
dizi = []

for i in range(adet):
    sayi = float(input(f"{i+1}. eleman: "))
    dizi.append(sayi)

yeni_dizi = [x * 5 for x in dizi]

print("Orijinal dizi:", dizi)
print("5 ile çarpılmış dizi:", yeni_dizi)
