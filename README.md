# BSM3517 - Bilimsel Hesaplama Yöntemleri: Derste Yapılan Temel Hesaplama Uygulamaları

Bu depo, **BSM3517 Bilimsel Hesaplama Yöntemleri** dersinde işlenen temel matematiksel ve mühendislik hesaplama uygulamalarını içermektedir.

## 📁 Kod Listesi ve Açıklamaları

1. **`arac_hiz_mesafe_hesaplayici.py`**: 90 km/s sabit hızla giden aracın girilen dakikada aldığı yol hesabı ($x = v \cdot t$).
2. **`dizi_bes_ile_carpma.py`**: Kullanıcıdan dinamik olarak alınan dizi elemanlarının 5 ile çarpılarak yeni diziye aktarılması.
3. **`dusey_atis_problemi.py`**: 120m yükseklikten $5\text{ m/s}$ ilk hızla aşağı atılan cismin 3 saniye sonraki yolu, yerden yüksekliği ve anlık hızı.
4. **`hafta1_sayfa5_daire_ve_hipotenus.py`**: Değişken tanımlama, daire alanı ($\pi r^2$) ve Pisagor teoremi ($c = \sqrt{a^2 + b^2}$).
5. **`hafta2_ornekler_sayfa5_guvenli_yaricap_while.py`**: `while` döngüsü ile negatif yarıçap girişlerini engelleyen güvenli veri doğrulama.
6. **`hafta3_numpy_tum_ornekler.py`**: NumPy kütüphanesinde `np.arange`, `np.linspace` ve 3x3 matris dilimleme (slicing) işlemleri.
7. **`hipotenus_hesaplayici.py`**: İki dik kenarı kullanıcıdan alıp Pisagor bağıntısıyla hipotenüsü hesaplama.
8. **`matris_3x3_yazdirma.py`**: 3x3 matrisi formatlı olarak ekrana yazdırma ve elemanlarının toplamını bulma.
9. **`np_dizi.py`**: `range(1, 11)` ile NumPy dizisi oluşturma; döngüyle ve vektörel (`dizi ** 2`) kare alma karşılaştırması.
10. **`numpy_dizi_reshape_ve_carpma.py`**: 12 elemanlı vektörü `reshape(3, 4)` ile matrise dönüştürme ve skaler 3 ile çarpma.
11. **`ozel_ucgenler_hipotenus.py`**: `[3, 4, 5, 12, 6, 8, 7, 24]` listesindeki ikili kenar çiftlerini ayırıp hipotenüslerini hesaplama.
12. **`sabit_ivmeli_hareket_t10.py`**: 5. Hafta 15. uygulama; $x(t) = v_0 t + \frac{1}{2} a t^2$ formülü ile $t=10$ saniyeye kadar ($0.5$ sn adımlarla) her zaman anındaki konumun ($x$) yazdırılması.
13. **`matris_10x10_ilk_son_satir_carpimi.py`**: 100 rastgele sayıdan (`np.random.randint`) 10x10 matris oluşturma; ilk ve son satırın eleman bazlı çarpımı, çarpım toplamı (`.sum()`), matrisin en büyük (`.max()`), en küçük (`.min()`) ve standart sapma (`.std()`) hesaplamaları.
14. **`rastgele_reshape_ve_vize_matrisi.py`**: 12 rastgele sayıyı `reshape(3, 4)` ile matrise çevirme; 70 üzeri değerlerden oluşan vize notları matrisi tanımlayıp `np.mean()` ile genel ortalama hesaplama.
