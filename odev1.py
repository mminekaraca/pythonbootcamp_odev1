print("Metin2 Evrenine Hoşgeldiniz!")

class Karakter:
    def __init__(self,ad,cinsiyet):
        self.ad = ad
        self.cinsiyet = cinsiyet

class Savasci(Karakter):
    def __init__(self,ad,cinsiyet,sinif):
        super().__init__(ad,cinsiyet)
        self.sinif = sinif

class Ninja(Karakter):
    def __init__(self,ad,cinsiyet,sinif):
        super().__init__(ad,cinsiyet)
        self.sinif = sinif

class Sura(Karakter):
    def __init__(self,ad,cinsiyet,sinif):
        super().__init__(ad,cinsiyet)
        self.sinif = sinif

class Saman(Karakter):
    def __init__(self,ad,cinsiyet,sinif):
        super().__init__(ad,cinsiyet)
        self.sinif = sinif

class Lycan(Karakter):
    def __init__(self,ad,cinsiyet,sinif):
        super().__init__(ad,cinsiyet)
        self.sinif = sinif


karakter_listesi = []

while True:
    print("""
-------------------
1. Savaşçı Ekle
2. Ninja Ekle
3. Sura Ekle
4. Şaman Ekle
5. Lycan Ekle
6. Karakter Listesi
7. Çıkış
-------------------
    """)
    secim = input("Seçiminiz: ")
    if secim == "1":
        ad = input("Adınızı Giriniz: ")
        cinsiyet = input("Cinsiyetinizi Giriniz: ")
        while True:
            sinif = input("Sınıfınızı Giriniz (Bedensel-Zihinsel): ")
            if sinif == "Bedensel" or sinif == "Zihinsel":
                karakter_listesi.append(Savasci(ad,cinsiyet,sinif))
                break
            else:
                print("Sınıf ancak Bedensel veya Zihinsel olabilir!")
    elif secim == "2":
        ad = input("Adınızı Giriniz: ")
        cinsiyet = input("Cinsiyetinizi Giriniz: ")
        while True:
            sinif = input("Sınıfınızı Giriniz (Uzak Dövüşçü-Yakın Dövüşçü): ")
            if sinif == "Uzak Dövüşçü" or sinif == "Yakın Dövüşçü":
                karakter_listesi.append(Ninja(ad,cinsiyet,sinif))
                break
            else:
                print("Sınıf ancak Uzak Dövüşçü veya Yakın Dövüşçü olabilir!")
    elif secim == "3":
        ad = input("Adınızı Giriniz: ")
        cinsiyet = input("Cinsiyetinizi Giriniz: ")
        while True:
            sinif = input("Sınıfınızı Giriniz (Karabüyü-Büyülü Silah): ")
            if sinif == "Karabüyü" or sinif == "Büyülü Silah":
                karakter_listesi.append(Sura(ad,cinsiyet,sinif))
                break
            else:
                print("Sınıf ancak Karabüyü veya Büyülü Silah olabilir!")
    elif secim == "4":
        ad = input("Adınızı Giriniz: ")
        cinsiyet = input("Cinsiyetinizi Giriniz: ")
        while True:
            sinif = input("Sınıfınızı Giriniz (Ejderha Gücü-İyileştirme): ")
            if sinif == "Ejderha Gücü" or sinif == "İyileştirme":
                karakter_listesi.append(Saman(ad,cinsiyet,sinif))
                break
            else:
                print("Sınıf ancak Ejderha Gücü veya İyileştirme olabilir!")
    elif secim == "5":
        ad = input("Adınızı Giriniz: ")
        cinsiyet = input("Cinsiyetinizi Giriniz: ")
        print("Lycan'lar sınıf seçimi yapamaz. İçgüdüleri çoktan seçimi yapmıştır.")
        karakter_listesi.append(Lycan(ad,cinsiyet,"İçgüdü"))
    elif secim == "6":
        print("\nToplam Karakter Sayısı: ",len(karakter_listesi))
        print("-----------------------------")
        print("Ad Cinsiyet Sınıf")
        for karakter in karakter_listesi:
            print(karakter.ad,karakter.cinsiyet,karakter.sinif)
    elif secim == "7":
        print("Programdan Çıkılıyor...")
        break
    else:
        print("Geçersiz Seçim!")
        