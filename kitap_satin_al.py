from PyQt5.QtWidgets import *
from kitap_satin_al_python import Ui_Form
from veritabani import veritabani



class KitapSatinAlSayfa(QWidget):
    
    def __init__(self):
        super().__init__()
        self.satinAlSayfa = Ui_Form()  
        self.satinAlSayfa.setupUi(self) 

        self.Sveritabani = veritabani()


        self.satinAlSayfa.satin_al_buton.clicked.connect(self.KitapAl)




    def KitapAl(self):
        _id = self.satinAlSayfa.id_line_edit.text()
        kitap_adi = self.satinAlSayfa.kitap_adi_line_edit.text()
        ad_soyad = self.satinAlSayfa.ad_soyad_line_Edit.text()
        adres = self.satinAlSayfa.adres_line_Edit.text()
        fiyat = self.satinAlSayfa.fiyat_line_edit.text()
        
        

        

        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            
            veriler = self.Sveritabani.SatinAl(_id, kitap_adi, ad_soyad,adres,fiyat)

        
        if veriler:
            
            QMessageBox.information(self, 'Başarılı', 'Satın Alma işleminiz Başarılı.')
        else:
            QMessageBox.warning(self, 'Hata', 'Satın alırken bir hata oldu .')
