from PyQt5.QtWidgets import *
from kitap_bilgi_sayfa_python import Ui_Form
from veritabani import veritabani


class KitapBilgiGoster(QWidget):
    
    def __init__(self):
        super().__init__()
        self.kitapbilgiGoster = Ui_Form()  
        self.kitapbilgiGoster.setupUi(self) 

        self.bveritabani = veritabani()
        self.kayitGoster()



        self.kitapbilgiGoster.arama_yap_line_edit.textChanged[str].connect(self.MusteriAra)


        



    def kayitGoster(self):
     kolonlar = ["ID", "KİTAP ADI", "SATIN ALAN KİŞİ", "ADRES", "YAPILAN ÖDEME"]
     self.kitapbilgiGoster.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.kitapbilgiGoster.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon  başlıklarını ayarla

     veriler = self.bveritabani.KitapkayitGoster()
     if veriler:
        self.kitapbilgiGoster.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.kitapbilgiGoster.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.kitapbilgiGoster.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Tablonun genişliğini ve sütunları ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Sütunları doldur
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(0, 80)  # ID sütununu 80 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(1, 200)  # KİTAP ADI sütununu 200 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(2, 150)  # SATIN ALAN KİŞİ sütununu 150 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(3, 250)  # ADRES sütununu 250 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(4, 120)  # YAPILAN ÖDEME sütununu 120 piksel olarak ayarla




    def MusteriAra(self):
     kolonlar = ["ID", "KİTAP ADI", "SATIN ALAN KİŞİ", "ADRES", "YAPILAN ÖDEME"]
     self.kitapbilgiGoster.bilgi_tableWidget.setColumnCount(len(kolonlar))  # Sütun sayısını ayarla
     self.kitapbilgiGoster.bilgi_tableWidget.setHorizontalHeaderLabels(kolonlar)  # Kolon  başlıklarını ayarla

     ad_soyad = self.kitapbilgiGoster.arama_yap_line_edit.text()

     veriler = self.bveritabani.MusteriAra(ad_soyad)
     if veriler:
        self.kitapbilgiGoster.bilgi_tableWidget.setRowCount(len(veriler))  # Satır sayısını ayarla
        for satir, veri in enumerate(veriler):
            self.kitapbilgiGoster.bilgi_tableWidget.setItem(satir, 0, QTableWidgetItem(str(veri[0])))  # ID değerini ekleyin
            for sutun, deger in enumerate(veri[1:], 1):  # 1'den başlayarak diğer sütunları ekleyin
                self.kitapbilgiGoster.bilgi_tableWidget.setItem(satir, sutun, QTableWidgetItem(str(deger)))

        # Tablonun genişliğini ve sütunları ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Sütunları doldur
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(0, 80)  # ID sütununu 80 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(1, 200)  # KİTAP ADI sütununu 200 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(2, 150)  # SATIN ALAN KİŞİ sütununu 150 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(3, 250)  # ADRES sütununu 250 piksel olarak ayarla
        self.kitapbilgiGoster.bilgi_tableWidget.setColumnWidth(4, 120)  # YAPILAN ÖDEME sütununu 120 piksel olarak ayarla











