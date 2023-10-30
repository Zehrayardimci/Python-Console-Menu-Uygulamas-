def k_kucuk(k, liste):

    if not isinstance(k, int):
        print("Hata: k değeri tam sayı olmalıdır.")
        return None

    if k > len(liste):
       print("Hata: k değeri listedeki eleman sayısından büyük olamaz.")
       return None

    if not liste:
        print("Hata: Liste boş olamaz.")
        return None

    if k <= 0:
        print("Hata: k değeri pozitif tam sayı olmalıdır.")
        return None

    sıralı_liste = sorted(liste)
    kucuk_eleman = sıralı_liste[k - 1]
    return kucuk_eleman

def en_yakin_cift(hedef, liste):
    if not isinstance(hedef, int):
        print("Hata: Hedef değer tam sayı olmalıdır.")
        return None

    if not liste:
        print("Hata: Liste boş olamaz.")
        return None

    if not all(isinstance(item, int) for item in liste):
        print("Hata: Liste elemanları tam sayı olmalıdır.")
        return None

    liste.sort()

    en_yakin_cift = None
    en_kucuk_fark = None

    for i in range(len(liste) - 1):
        for j in range(i + 1, len(liste)):
            toplam = liste[i] + liste[j]
            fark = abs(hedef - toplam)

            if en_kucuk_fark is None or fark < en_kucuk_fark:
                en_kucuk_fark = fark
                en_yakin_cift = (liste[i], liste[j])

    if en_yakin_cift:
        return en_yakin_cift, sum(en_yakin_cift)
    else:
        print("Verilen hedefe en yakın çift bulunamadı.")
        return None

def tekrar_eden_elemanlar(liste):
    if not liste:
        print("Hata: Liste boş olamaz. Lütfen geçerli bir liste girin.")
        return None

    if not all(isinstance(item, int) for item in liste):
        print("Hata: Liste elemanları tam sayı olmalıdır.")
        return None

    tekrar_edenler = list(set([eleman for eleman in liste if liste.count(eleman) > 1]))
    return tekrar_edenler

def matris_carpimi(matris1, matris2):
    if not matris1 or not matris2:
        print("Hata: Matrisler boş olamaz.")
        return None

    m = len(matris1)
    n = len(matris1[0])
    p = len(matris2)
    q = len(matris2[0])

    if n != p:
        print("Hata: İlk matrisin sütun sayısı ikinci matrisin satır sayısına eşit olmalıdır.")
        return None

    sonuc = [[sum(eleman1 * eleman2 for eleman1, eleman2 in zip(satir1, satir2)) for satir2 in zip(*matris2)] for satir1 in matris1]
    return sonuc


from functools import reduce

def kelime_frekansi_bul(dosya_konumu):
    try:
        with open(dosya_konumu, 'r') as dosya:
            metin = dosya.read()

        kelimeler = metin.split()

        def kelime_frekansi(kelime):
            return reduce(lambda x, y: x + 1 if y == kelime else x, kelimeler, 0)

        kelime_listesi = list(set(kelimeler))
        frekanslar = list(map(kelime_frekansi, kelime_listesi))

        kelime_frekans_dict = dict(zip(kelime_listesi, frekanslar))
        return kelime_frekans_dict

    except FileNotFoundError:
        return "Dosya bulunamadı. Lütfen doğru dosya konumunu girin."

def en_kucuk_deger(liste):
    if not liste:
        print("Hata: Liste boş olamaz.")
        return None

    if len(liste) == 1:
        return liste[0]
    else:
        min_deger_sonrasi = en_kucuk_deger(liste[1:])
        return liste[0] if liste[0] < min_deger_sonrasi else min_deger_sonrasi


def karekok(N, x0, tol=1e-10, maxiter=10):
    if N < 0:
        print("Hata: Negatif sayılar için karekök hesaplanamaz.")
        return None

    if not isinstance(tol, (float, int)) or tol <= 0:
        print("Hata: Geçersiz tolerans değeri. Tolerans pozitif bir sayı olmalıdır.")
        return None

    if not isinstance(maxiter, int) or maxiter <= 0:
        print("Hata: Geçersiz maksimum iterasyon sayısı. Maksimum iterasyon pozitif bir tam sayı olmalıdır.")
        return None

    def iterasyon(tahmin, iterasyon_sayisi):
        yeni_tahmin, hata = karekok_iterasyon(N, tahmin, tol)
        iterasyon_sayisi += 1

        if hata < tol or iterasyon_sayisi >= maxiter:
            return yeni_tahmin
        else:
            return iterasyon(yeni_tahmin, iterasyon_sayisi)

    return iterasyon(x0, 0)


def karekok_iterasyon(N, tahmin, tol=1e-10):
    yeni_tahmin = 0.5 * (tahmin + N / tahmin)
    hata = abs(yeni_tahmin ** 2 - N)

    if hata < tol:
        return yeni_tahmin, hata
    else:
        return karekok_iterasyon(N, yeni_tahmin, tol)

def eb_ortak_bolen(a, b):
    if a < 0 or b < 0:
        print("Hata: Negatif sayılar için EBOB hesaplanamaz.")
        return None

    if not isinstance(a, int) or not isinstance(b, int):
        print("Hata: Tam sayı olmayan değerler için EBOB hesaplanamaz.")
        return None

    if a == 0 or b == 0:
        print("Hata: Sıfırın EBOB'u yoktur.")
        return None

    return eb_ortak_bolen_recursive(a, b)

def eb_ortak_bolen_recursive(a, b):
    if b == 0:
        return a
    else:
        return eb_ortak_bolen_recursive(b, a % b)


def asal_veya_degil(n, i=2):
    if n <= 1:
        print("Hata: Asal sayılar 1'den büyük olmalıdır.")
        return None

    if not isinstance(n, int):
        print("Hata: Tam sayı olmayan değerler için asal sayı kontrolü yapılamaz.")
        return None

    if n == i:
        return True
    if n % i == 0:
        return False

    return asal_veya_degil(n, i + 1)


def hizlandirici(n, k, fib_k, fib_k1):
    if k == n:
        return fib_k

    yeni_fib = fib_k + fib_k1
    return hizlandirici(n, k + 1, yeni_fib, fib_k)


def fibonacci_hizlandirici(n):
    if n <= 0:
        print("Hata: Geçersiz Fibonacci sayısı. Fibonacci sayısı pozitif tam sayı olmalıdır.")
        return None

    if not isinstance(n, int):
        print("Hata: Geçersiz Fibonacci sayısı. Fibonacci sayısı tam sayı olmalıdır.")
        return None

    max_fibonacci_number = 1000000
    if n > max_fibonacci_number:
        print("Hata: Çok büyük bir Fibonacci sayısı hesaplanıyor. Daha küçük bir sayı deneyin.")
        return None

    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return hizlandirici(n, 3, 1, 1)

while True:
    print("\nMenü:")
    print("1. K küçük")
    print("2. En yakın çift")
    print("3. Tekrar eden elemanlar")
    print("4. Matris çarpımı")
    print("5. Kelime frekansı bulma")
    print("6. En küçük değer")
    print("7. Karekök hesaplama")
    print("8. EBOB hesaplama")
    print("9. Asal sayı kontrolü")
    print("10. Fibonacci hesaplama")
    print("11. Çıkış")

    secim = input("Lütfen bir seçenek numarası girin (1-11): ")

    if secim == "1":
        k = int(input("k değerini girin: "))
        liste = list(map(int, input("Bir liste girin (virgülle ayrılmış): ").split(",")))
        sonuc = k_kucuk(k, liste)
        print(f"K. küçük eleman: {sonuc}")

    elif secim == "2":
        hedef = int(input("Hedef değeri girin: "))
        liste = list(map(int, input("Bir liste girin (virgülle ayrılmış): ").split(",")))
        sonuc = en_yakin_cift(hedef, liste)
        print(f"En yakın çift: {sonuc[0]}, Toplam: {sonuc[1]}")

    elif secim == "3":
        liste = list(map(int, input("Bir liste girin (virgülle ayrılmış): ").split(",")))
        sonuc = tekrar_eden_elemanlar(liste)
        print(f"Tekrar eden elemanlar: {sonuc}")

    elif secim == "4":
        matris1 = [[int(x) for x in input("Matris 1'i girin (virgülle ayrılmış): ").split(",")] for _ in range(int(input("Matris 1'in satır sayısını girin: ")))]
        matris2 = [[int(x) for x in input("Matris 2'yi girin (virgülle ayrılmış): ").split(",")] for _ in range(int(input("Matris 2'nin satır sayısını girin: ")))]
        sonuc = matris_carpimi(matris1, matris2)
        print(f"Matris çarpımı: {sonuc}")

    elif secim == "5":
        dosya_konumu = input("Dosya konumunu girin: ")
        sonuc = kelime_frekansi_bul(dosya_konumu)
        print(f"Kelime frekansları: {sonuc}")

    elif secim == "6":
        liste = list(map(int, input("Bir liste girin (virgülle ayrılmış): ").split(",")))
        sonuc = en_kucuk_deger(liste)
        print(f"En küçük değer: {sonuc}")

    elif secim == "7":
        N = int(input("Karekök alınacak sayıyı girin: "))
        tahmin = float(input("Başlangıç tahminini girin: "))
        tol = float(input("Tolerans değerini girin: "))
        maxiter = int(input("Maksimum iterasyon sayısını girin: "))
        sonuc = karekok(N, tahmin, tol, maxiter)
        print(f"Karekök: {sonuc}")

    elif secim == "8":
        a = int(input("Birinci sayıyı girin: "))
        b = int(input("İkinci sayıyı girin: "))
        sonuc = eb_ortak_bolen(a, b)
        print(f"EBOB: {sonuc}")

    elif secim == "9":
        n = int(input("Asal sayı olup olmadığını kontrol etmek istediğiniz sayıyı girin: "))
        sonuc = asal_veya_degil(n)
        if sonuc:
            print("Bu bir asal sayıdır.")
        else:
            print("Bu bir asal sayı değildir.")

    elif secim == "10":
        n = int(input("Fibonacci hesaplamak istediğiniz sayıyı girin: "))
        sonuc = fibonacci_hizlandirici(n)
        print(f"Fibonacci sayısı: {sonuc}")

    elif secim == "11":
        print("Programdan çıkılıyor.")
        break

    else:
        print("Geçersiz bir seçenek girdiniz. Lütfen tekrar deneyin.")