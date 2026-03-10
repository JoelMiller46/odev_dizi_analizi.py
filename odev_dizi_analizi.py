# odev_dizi_analizi.py
# Ders: Veri Yapıları ve Algoritmalar
# Konu: Dizi Analizi Programı

# ==========================================
# BÖLÜM 1: KULLANICIDAN VERİ ALMA
# ==========================================
adet = int(input("Kaç sayı gireceksiniz: "))
dizi = []

for i in range(adet):
    sayi = int(input(f"Sayı {i+1}: "))
    dizi.append(sayi)

# ==========================================
# BÖLÜM 2: DİZİ ANALİZİ
# ==========================================
# Hazır fonksiyon kullanmadan döngü ile analiz yapıyoruz
toplam = 0
en_buyuk = dizi[0]
en_kucuk = dizi[0]

for sayi in dizi:
    toplam += sayi # Toplamı hesapla
    
    if sayi > en_buyuk: # En büyüğü bul
        en_buyuk = sayi
        
    if sayi < en_kucuk: # En küçüğü bul
        en_kucuk = sayi

ortalama = toplam / adet

print(f"\nToplam: {toplam}")
print(f"Ortalama: {ortalama}")
print(f"En büyük sayı: {en_buyuk}")
print(f"En küçük sayı: {en_kucuk}")

# ==========================================
# BÖLÜM 3: ÖZEL ANALİZ
# ==========================================
cift_sayisi = 0
tek_sayisi = 0
ondan_buyuk = 0

for sayi in dizi:
    # Çift/Tek kontrolü (Modüler aritmetik)
    if sayi % 2 == 0:
        cift_sayisi += 1
    else:
        tek_sayisi += 1
        
    # 10'dan büyük olma durumu
    if sayi > 10:
        ondan_buyuk += 1

print(f"\nÇift sayı sayısı: {cift_sayisi}")
print(f"Tek sayı sayısı: {tek_sayisi}")
print(f"10'dan büyük sayı sayısı: {ondan_buyuk}")

# ==========================================
# BÖLÜM 4: DİZİYİ TERS YAZDIRMA
# ==========================================
print(f"\nOrijinal dizi: {dizi}\n")
print("Ters dizi:")

# İndeksleri sondan başa doğru (adet-1'den 0'a kadar) döndürüyoruz
for i in range(adet - 1, -1, -1):
    print(dizi[i], end=" ")
print() # Alt satıra düzgün geçmek için

# ==========================================
# BÖLÜM 5: SAYI ARAMA
# ==========================================
aranan = int(input("\nAranacak sayı: "))
bulundu_mu = False

for sayi in dizi:
    if sayi == aranan:
        bulundu_mu = True
        break # Sayıyı bulduktan sonra döngüyü boşuna uzatmamak için kırıyoruz

if bulundu_mu:
    print("Sayı dizide bulundu")
else:
    print("Sayı dizide bulunamadı")

# ==========================================
# BONUS BÖLÜM 
# ==========================================
print("\n--- BONUS ÖZELLİKLER ---")

# 1. Negatif sayıları listeleme
negatifler = []
for sayi in dizi:
    if sayi < 0:
        negatifler.append(str(sayi))

if len(negatifler) > 0:
    print(f"Negatif sayılar: {', '.join(negatifler)}")
else:
    print("Dizide negatif sayı yok.")

# 2. Ortalamanın üzerindeki sayıları yazdırma
ortalamadan_buyukler = []
for sayi in dizi:
    if sayi > ortalama:
        ortalamadan_buyukler.append(str(sayi))

if len(ortalamadan_buyukler) > 0:
    print(f"Ortalamanın üzerindeki sayılar: {', '.join(ortalamadan_buyukler)}")
else:
    print("Ortalamanın üzerinde sayı yok.")

# 3. En çok tekrar eden sayıyı bulma (Frekans analizi)
frekanslar = {}
for sayi in dizi:
    if sayi in frekanslar:
        frekanslar[sayi] += 1
    else:
        frekanslar[sayi] = 1

en_cok_tekrar_eden = dizi[0]
en_yuksek_frekans = 0

for sayi, frekans in frekanslar.items():
    if frekans > en_yuksek_frekans:
        en_yuksek_frekans = frekans
        en_cok_tekrar_eden = sayi

if en_yuksek_frekans > 1:
    print(f"En çok tekrar eden sayı: {en_cok_tekrar_eden} ({en_yuksek_frekans} kez tekrar etti)")
else:
    print("Dizideki tüm sayılar birbirinden farklı, tekrar eden sayı yok.")