"""class <Class Ismi>():   #class isimleri, genelin aksine büyük harfle başlar

    <class attr>           # class attribute, oluşturulanın aksine genel değerleri içerir.

    def __init__(self,<attr>):       #init, instantiation yani örneklendirmenin kisaltmasidir.
        self.<instance attr> = attr  #instance attribute'ler, oluşturulan örneğe özgüdür.
        ...

    def <methods>(self,<params>):    # methodlar class'a özgü fonksiyonlardır.
         ...
         return ...                              """

class Ucus():
    havayolu="THY"

    def __init__(self,kod,kalkis,varis,sure,kapasite,yolcu):
        self.kod=kod
        self.kalkis=kalkis
        self.varis=varis
        self.sure=sure
        self.kapasite=kapasite
        self.yolcu=yolcu

    def anons_yap(self):
        return "{} sefer sayili {}-{} ucusumuz {} dakika sürecektir.".format(self.kod,
        self.kalkis,self.varis,self.sure)


    def koltuk_sayisi_guncelle(self):
        return self.kapasite - self.yolcu

    def bilet_satis(self,bilet_adedi=1):
        if self.yolcu + bilet_adedi <= self.kapasite:
            self.yolcu += bilet_adedi
            self.koltuk_sayisi_guncelle()
            print("{} adet bilet satilmıştır, kalan koltuk sayısı {}".format(
                bilet_adedi,self.koltuk_sayisi_guncelle()))

        else:
            print("{} İşlem gerçekleştirilemedi. Yetersiz koltuk sayısı...")

    def bilet_iptal(self,bilet_adedi=1):
        if self.yolcu >= bilet_adedi:
            self.yolcu -= bilet_adedi
            print("{} adet bilet iptal edilmiştir, güncel koltuk sayısı {}".format(
                bilet_adedi,self.koltuk_sayisi_guncelle()))

        else:
            print("İşlem gerçekleştirilemedi, iptal edilecek kadar yolcu yok...")



ucus1=Ucus("TK123","TRA","İST",60,250,200)
print(ucus1.anons_yap())
print(ucus1.koltuk_sayisi_guncelle())

print(ucus1.bilet_satis(5))

print(ucus1.bilet_satis(10))

print(ucus1.bilet_iptal(10))

print(ucus1.koltuk_sayisi_guncelle())