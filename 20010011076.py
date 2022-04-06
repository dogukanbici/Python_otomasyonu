#DOGUKAN BİCİ 20010011076
import sys
def menuTasarim():
    print("------------------------OTO AKSESUAR SATIŞ OTOMASYONU------------------------")
    while True:
        print("1-Sipariş Ekleme\n"
              "2-Sipariş Silme\n"
              "3-Sipariş Güncelle\n"
              "4-Sipariş Listele\n"
              "5-Sipariş Arama\n"
              "6-Toplam Sipariş Öğrenme\n"
              "7-Toplam Kazanç Öğrenme\n"
              "8-Çıkış\n")
        secim = input("Seçiminiz:")
        if secim == "1":
            islemler(1)
        elif secim == "2":
            islemler(2)
        elif secim == "3":
            islemler(3)
        elif secim == "4":
            islemler(4)
        elif secim == "5":
            islemler(5)
        elif secim == "6":
            islemler(6)
        elif secim == "7":
            islemler(7)
        elif secim == "8":
            sys.exit()
        else:
            print("Hatalı bir seçim yaptınız")
def islemler(islemNo):
    if (islemNo==1):
        def siparisEkle():
            print("------------------------SİPARİŞ EKLEME------------------------")
            with open("20010011076.txt","a",encoding="utf-8") as dosya:
                siparisAdet = int(input("Kaç adet sipariş gireceksiniz: "))
                siparisler={}
                for i in range(siparisAdet):
                    siparis = dict()
                    siparisNo= input(f"{i+1}. sipariş numarasi:")
                    siparis1= input(f"{i+1}. sipariş içeriği:")
                    adet = input(f"{i+1}. sipariş içeriği adet:")
                    fiyat = input(f"{i+1}. sipariş içeriği fiyat:")
                    adres = input(f"{i+1}. siparişin adresi(Bayi):")
                    siparis["siparis detay"]= siparis1
                    siparis["sipariş içeriği adet"]= adet + " adet"
                    siparis["sipariş fiyat"]= fiyat + " TL"
                    siparis["sipariş adres"]= adres
                    siparisler[siparisNo + " nolu sipariş"] = siparis
                for key in siparisler.keys():
                    dosya.write(str(key) + " ")
                    for value in siparisler[key].values():
                        dosya.write(value + " ")
                    dosya.write("\n")
                print("Sipariş Eklendi.")
        siparisEkle()
    elif (islemNo==2):
        def siparisSilme():
            print("------------------------SİPARİŞ SİLME------------------------")
            with open("20010011076.txt","r",encoding="utf-8") as dosya:
                durum= None
                siparisler = {}
                siparisNo = input("Silmek istediğiniz sipariş nosunu giriniz:")
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0],eleman[1:]
                    siparisler[key]=value
                    if siparisNo==key:
                        durum = True
                        siparisler.pop(key)
                if durum:
                    with open("20010011076.txt","w",encoding="utf-8")as ds:
                        for key in siparisler.keys():
                            ds.write(key)
                            for i in range(len(siparisler[key])):
                                ds.write(" "+siparisler[key][i])
                    print("Silme işleminiz gerçekleşmiştir.")
                else:
                    print("Silmek istediğiniz sipariş bulunamamıştır.")
        siparisSilme()
    elif (islemNo == 3):
        def siparisGuncelleme():
            print("------------------------SİPARİŞ GÜNCELLEME------------------------")
            with open("20010011076.txt","r",encoding="utf-8") as dosya:
                durum= None
                siparisler = {}
                siparis= []
                siparisNo = input("Güncellemek istediğiniz sipariş nosunu giriniz:")
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0], eleman[1:]
                    siparisler[key]=value
                    if siparisNo==key:
                        durum = True
                        siparis1 = input(f"{siparisNo}. siparişin yeni sipariş içeriği:")
                        adet = input(f"{siparisNo}.siparişin yeni sipariş içeriği adet:")
                        fiyat = input(f"{siparisNo}. siparişin yeni sipariş içeriği fiyat:")
                        adres = input(f"{siparisNo}. siparişin yeni sipariş adresi(Bayi):")
                        siparis.append("nolu sipariş")
                        siparis.append(siparis1)
                        siparis.append(adet + " adet")
                        siparis.append(fiyat + " TL")
                        siparis.append(adres)
                        siparisler[siparisNo] = siparis
                if durum:
                    with open("20010011076.txt","w",encoding="utf-8")as ds:
                        for key in siparisler.keys():
                            ds.write(key)
                            for i in range(len(siparisler[key])):
                                ds.write(" "+siparisler[key][i])
                    print("Güncelleme işleminiz gerçekleşmiştir.")
                else:
                    print("Güncellemek istediğiniz sipariş bulunamamıştır.")
        siparisGuncelleme()
    elif (islemNo == 4):
        def siparisListeleme():
            print("------------------------SİPARİŞ LİSTELEME------------------------")
            with open("20010011076.txt","r",encoding="utf-8") as dosya:
                siparisler = {}
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0],eleman[1:]
                    siparisler[key]=value
                for key in siparisler.keys():
                    print(key, end=" ")
                    for i in range(len(siparisler[key])):
                        print(siparisler[key][i], end=" ")
                    print("\n")
        siparisListeleme()
    elif (islemNo == 5):
        def siparisArama():
            print("------------------------SİPARİŞ ARAMA------------------------")
            with open("20010011076.txt", "r", encoding="utf-8") as dosya:
                siparisler = {}
                siparisNo = input("Aramak istediğiniz sipariş nosunu giriniz:")
                for line in dosya.readlines():
                    eleman = line.split(" ")
                    key, value = eleman[0], eleman[1:]
                    siparisler[key] = value
                    if siparisNo==key:
                        print(key, end=" ")
                        for i in range(len(siparisler[key])):
                            print(siparisler[key][i], end=" ")
                        print("\n")
        siparisArama()
    elif (islemNo == 6):
        def toplamSiparis():
            with open("20010011076.txt", "r", encoding="utf-8") as dosya:
                kayitlar=0
                for line in dosya.readlines():
                    kayitlar=kayitlar+1
                print(str(kayitlar) +" tane sipariş var")
        toplamSiparis()
    elif (islemNo == 7):
        def toplamKazanc():
            with open("20010011076.txt","r",encoding="utf-8") as dosya:
                toplam=0
                for line in dosya.readlines():
                    syc = 0
                    eleman = line.split(" ")
                    for e in eleman:
                        if (e=="TL"):
                            toplam = toplam + int(eleman[syc-1])
                        syc = syc + 1
                print(toplam)
        toplamKazanc()
menuTasarim()
