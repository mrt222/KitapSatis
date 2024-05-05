from PyQt5.QtWidgets import *
from anapencere_python_ import Ui_MainWindow
from kitap_duzenle_ import DuzenleSayfa
from veritabani import veritabani
from kitap_satin_al import KitapSatinAlSayfa
from kitap_bilgi_sayfa import KitapBilgiGoster

class Anapencere(QMainWindow):
    def __init__(self):
        super().__init__()
        self.anapencere = Ui_MainWindow()
        self.anapencere.setupUi(self)

        self.duzenlesayfa = DuzenleSayfa()
        self.anapencere.Kitap_duzenle_sayfa.triggered.connect(self.DuzenleFormu)

        self.satinAlSayfa = KitapSatinAlSayfa()

        self.anapencere.kitap_satin_al_sayfa.triggered.connect(self.SatinAlformu)


        self.kitapBilgiGoster = KitapBilgiGoster()

        self.anapencere.satilan_kitap_sayfa.triggered.connect(self.KitapGoster)
        
        


        self.anaveritabani = veritabani()
        self.kayitGoster()


        self.anapencere.arama_yap_line_edit.textChanged[str].connect(self.KitapAra)


    def DuzenleFormu(self):
        self.duzenlesayfa.show()


    def SatinAlformu(self):
       self.satinAlSayfa.show()



    def KitapGoster(self):
       self.kitapBilgiGoster.show()



    def kayitGoster(self):
     kolonlar = ["ID", "KİTAP ADI", "YAZAR ADI", "SAYFA SAYISI", "KATEGORİ","FİYAT","EKLENDİĞİ TARİH"]
     self.anapencere.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencere.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla

     veriler = self.anaveritabani.kayitGoster()
     if veriler:
        self.anapencere.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencere.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencere.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

     # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.anapencere.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)


    def KitapAra(self):
     kolonlar = ["ID", "KİTAP ADI", "YAZAR ADI", "SAYFA SAYISI", "KATEGORİ","FİYAT","EKLENDİĞİ TARİH"]
     self.anapencere.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.anapencere.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon başlıklarını ayarla
     ad_soyad= self.anapencere.arama_yap_line_edit.text()

     veriler = self.anaveritabani.MusteriAra(ad_soyad)
     if veriler:
        self.anapencere.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.anapencere.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.anapencere.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

    # Tablonun genişliğini sığabilecek şekilde ayarlayın
     self.anapencere.bilgi_tableWidget.horizontalHeader().setStretchLastSection(True)

app = QApplication([])
pencere = Anapencere()  
pencere.show()
app.exec_()
       
