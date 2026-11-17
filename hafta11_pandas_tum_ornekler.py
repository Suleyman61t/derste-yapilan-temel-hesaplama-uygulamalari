# -*- coding: utf-8 -*-
"""
BSM3517 Bilimsel Hesaplama Yöntemleri - 11. Hafta (Pandas Kütüphanesi)
HAFTA11.pdf Ders Notundaki Tüm Örnekler ve Uygulamalar Tek Dosyada Konsolide Edilmiştir.
"""

import numpy as np
import pandas as pd

# ==============================================================================
# ÖRNEK 1: PANDAS SERİSİ OLUŞTURMA (LİSTE VE DİZİ İLE) - SAYFA 1
# ==============================================================================
# Soru: Verilen etiket ve veri listeleriyle Pandas serisi oluşturunuz.
# Burada pd.Series() fonksiyonuna veri ve etiket listesini vererek seriler ürettik.

print("=" * 60)
print("ÖRNEK 1: PANDAS SERİLERİ (LİSTE VE NUMPY DİZİSİ İLE)")
print("=" * 60)

# 1.1. Python Listeleri ile Seri
label_list = ['I', 'am', 'Learning', 'Data', 'Science']
data_list = [1, 2, 3, 4, 5]
pd_series1 = pd.Series(data_list, index=label_list)
print("1.1. Etiketli Seri 1:\n", pd_series1)

# 1.2. NumPy Dizisi ve range() ile Seri
data_np = np.array(['a', 'b', 'c', 'd'])
pd_series2 = pd.Series(data_np, index=[*range(1, 5)])
print("\n1.2. range(1, 5) İndeksli Seri:\n", pd_series2)


# ==============================================================================
# ÖRNEK 2: SÖZLÜKLERDEN SERİ OLUŞTURMA, SERİ ARİTMETİĞİ VE BİRLEŞTİRME - SAYFA 2
# ==============================================================================
# Soru: Sözlükler üzerinden seriler tanımlayıp toplama ve ekleme (append) işlemlerini yapınız.
# Burada sözlükleri seriye çevirip indeks eşleşmesiyle topladık; ortak olmayan indekslerde NaN oluştuğunu gördük.

print("\n" + "=" * 60)
print("ÖRNEK 2: SÖZLÜKLERLE SERİLER, TOPLAMA VE BİRLEŞTİRME")
print("=" * 60)

DataDict = {'Yemek': 17000, 'Ulaşım': 28000}
A = pd.Series(DataDict)

DataDict2 = {'Yemek': 22000, 'Ulaşım': 15000}
B = pd.Series(DataDict2)

DataDict3 = {'Tatil': 15000, 'Yemek': 20000}
C = pd.Series(DataDict3)

print("A Serisi:\n", A)
print("\nB Serisi:\n", B)
print("\nC Serisi:\n", C)

# Serilerde Toplama (Aynı etiketler toplanır)
toplam_AB = A + B
print("\nA + B Toplamı:\n", toplam_AB)

# Eşleşmeyen etiketlerde NaN (Not a Number) oluşur
toplam_ABC = A + B + C
print("\nA + B + C Toplamı (NaN Durumu):\n", toplam_ABC)

# Serileri alt alta ekleme (_append / concat)
DataDict4 = pd.concat([C, A])  # veya C._append(A)
print("\nC Serisine A'nın Eklenmesi:\n", DataDict4)


# ==============================================================================
# ÖRNEK 3: DATAFRAME OLUŞTURMA TEMELLERİ (RANDOM VE SÖZLÜK) - SAYFA 2 & 3
# ==============================================================================
# Soru: Rastgele sayılar ve sözlükler ile DataFrame tabloları oluşturunuz.
# Burada randn, sözlük ve randint ile satır-sütun etiketli tablolar ürettik.

print("\n" + "=" * 60)
print("ÖRNEK 3: DATAFRAME OLUŞTURMA YÖNTEMLERİ")
print("=" * 60)

# 3.1. randn(5, 5) ile DataFrame
from numpy.random import randn
df_random = pd.DataFrame(
    data=randn(5, 5),
    index=['A', 'B', 'C', 'D', 'E'],
    columns=['Columns1', 'Columns2', 'Columns3', 'Columns4', 'Columns5']
)
print("3.1. 5x5 Rastgele DataFrame:\n", df_random)

# 3.2. Sözlük ile Basit DataFrame
df_yes_no = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]})
print("\n3.2. Sözlük ile Basit DataFrame:\n", df_yes_no)

# 3.3. Özel İndeksli Ürünler Tablosu (randint ile)
datalist = np.random.randint(100, size=(4, 2))
Ozellikler = ["Yes", "No"]
Urunler = ["Ürün 1", "Ürün 2", "Ürün 3", "Ürün 4"]
df_urunler = pd.DataFrame(data=datalist, index=Urunler, columns=Ozellikler)
print("\n3.3. Ürünler ve Özellikler Tablosu:\n", df_urunler)

# DataFrame Özellikleri (ndim, shape vb.)
print(f"\nTablo Boyut Sayısı (ndim) : {df_urunler.ndim}")
print(f"Tablo Biçimi (shape)      : {df_urunler.shape}")


# ==============================================================================
# ÖRNEK 4: DERSİN ÖRNEK UYGULAMASI (50 ÖĞRENCİ VİZE, ÖDEV, FİNAL TABLOSU) - SAYFA 3 & 4
# ==============================================================================
# Soru: 50 kişilik bir öğrenci grubunun vize (25-85), ödev (50-100) ve final (30-90)
# notlarının yer aldığı float tipinde (2 ondalık basamaklı) DataFrame tablosunu oluşturunuz.
# Not dizilerini tek bir matriste (np.array().T) birleştirerek DataFrame'e aktarınız.
# İndeksler 'Öğrenci 1', 'Öğrenci 2', ..., 'Öğrenci 50' olmalıdır.

print("\n" + "=" * 60)
print("ÖRNEK 4: SLAYTTAKİ RESMİ ÖRNEK UYGULAMA (50 ÖĞRENCİ NOT TABLOSU)")
print("=" * 60)

np.random.seed(42)  # Tekrarlanabilir rastgelelik için

# 50 öğrenci için belirlenen aralıklarda rastgele float notlar (2 basamak yuvarlama)
vize = np.round(np.random.uniform(25, 86, 50), 2)
odev = np.round(np.random.uniform(50, 101, 50), 2)
final = np.round(np.random.uniform(30, 91, 50), 2)

# Vize, Ödev ve Final dizilerini tek bir 2B matriste birleştirme (.T transpoz ile sütunlara dağıtma)
notlar_matrisi = np.array([vize, odev, final]).T

# Öğrenci 1'den 50'ye kadar indeks listesi
ogrenci_indeksleri = [f"Öğrenci {i}" for i in range(1, 51)]

# Ortak matris üzerinden DataFrame oluşturma
not_tablosu = pd.DataFrame(
    data=notlar_matrisi,
    columns=["Vize", "Ödev", "Final"],
    index=ogrenci_indeksleri
)

print("Not Tablosu (İlk 5 ve Son 5 Öğrenci):\n", not_tablosu.head(5))
print("...\n", not_tablosu.tail(5))

# İstatistiksel özet (mean, min, max, std)
print("\nNotların İstatistiksel Özeti (Ortalama, Min, Max, Std):")
print(not_tablosu.describe().loc[['mean', 'min', 'max', 'std']])


# ==============================================================================
# ÖRNEK 5: DATAFRAME VERİ SEÇİMİ (LOC VE ILOC FARK VE KULLANIMLARI) - SAYFA 4, 6 & 7
# ==============================================================================
# Soru: DataFrame üzerinde sütun seçimi, .loc (etiket bazlı) ve .iloc (indeks bazlı)
# filtreleme ve dilimleme işlemlerini gösteriniz.

print("\n" + "=" * 60)
print("ÖRNEK 5: VERİ SEÇİMİ (.loc VE .iloc İLE DİLİMLEME)")
print("=" * 60)

# Sütun seçimi
print("Sadece Final Sütunu (İlk 3 Eleman):\n", not_tablosu['Final'].head(3))

# loc (Etiket / İsim bazlı seçim)
print("\n--- LOC (Etiket Bazlı Seçim) ---")
print("1) 'Öğrenci 1'den 'Öğrenci 3'e kadar 'Vize' ve 'Final' sütunları:")
print(not_tablosu.loc['Öğrenci 1':'Öğrenci 3', ['Vize', 'Final']])

print("\n2) Final notu 80'in üzerinde olan başarılı öğrenciler (Filtreleme):")
basarili_final = not_tablosu.loc[not_tablosu['Final'] >= 80]
print(basarili_final.head(4))

print("\n3) Vizesi 70 üstü VE Finali 80 üstü olan öğrenciler (Çift Koşul - &):")
cift_kosul = not_tablosu.loc[(not_tablosu['Vize'] >= 70) & (not_tablosu['Final'] >= 80)]
print(cift_kosul)

# iloc (Tamsayı / İndeks pozisyonu bazlı seçim)
print("\n--- ILOC (Pozisyon Bazlı İndeksleme) ---")
print("1) İlk 3 satır ve ilk 2 sütun (0:3, 0:2):")
print(not_tablosu.iloc[:3, :2])

print("\n2) 2. satırdan 5. satıra kadar (index 2:5) sadece Final sütunu (index 2):")
print(not_tablosu.iloc[2:5, 2])

print("\n" + "=" * 60)
print("HAFTA 11 TÜM UYGULAMALARI BAŞARIYLA ÇALIŞTIRILDI!")
print("=" * 60)
