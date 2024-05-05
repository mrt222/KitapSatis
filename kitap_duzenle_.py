from PyQt5.QtWidgets import *
from kitap_duzenle_python import Ui_Form
from veritabani import veritabani



class DuzenleSayfa(QWidget):
   
    def __init__(self):
        super().__init__()
        self.duzenlesayfa = Ui_Form()  
        self.duzenlesayfa.setupUi(self) 

        self.dveritabani = veritabani()
        
        
        self.duzenlesayfa.ekle_button.clicked.connect(self.KitapEkle)
        self.duzenlesayfa.sil_button.clicked.connect(self.Kitapsil)
        self.duzenlesayfa.guncelle_button.clicked.connect(self.KitapGuncelle)


        
        


    def KitapEkle(self):
        _id = self.duzenlesayfa.id_line_edit.text()
        kitap_adi = self.duzenlesayfa.kitap_adi_line_edit.text()
        yazar_adi = self.duzenlesayfa.yazar_adi_line_edit.text()
        sayfa_sayisi = self.duzenlesayfa.sayfa_sayisi_line_edit.text()
        kategori = self.duzenlesayfa.kategori_line_edit.text()
        fiyat = self.duzenlesayfa.fiyat_line_Edit.text()
        eklendigi_tarih = self.duzenlesayfa.eklendigi_tarih_line_edit.text()

        

        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            self.listeSinyali.emit()
            veriler = self.dveritabani.kayitEkle(_id, kitap_adi, yazar_adi, sayfa_sayisi, kategori, fiyat, eklendigi_tarih)

        
        if veriler:
            self.listeSinyali.emit()
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla eklendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt eklenirken bir hata oluştu.')


    def Kitapsil(self):
        _id = self.duzenlesayfa.id_line_edit.text()
        sil = self.dveritabani.sil(_id)

        if sil:
            self.listeSinyali.emit()
            QMessageBox.information(self,"Bilgi","Kayıt Başarıyla Silindi")
        else:
            QMessageBox.warning(self,"Bilgi","Kayıt Silinemedi.")





    def KitapGuncelle(self):
        _id = self.duzenlesayfa.id_line_edit.text()
        kitap_adi = self.duzenlesayfa.kitap_adi_line_edit.text()
        yazar_adi = self.duzenlesayfa.yazar_adi_line_edit.text()
        sayfa_sayisi = self.duzenlesayfa.sayfa_sayisi_line_edit.text()
        kategori = self.duzenlesayfa.kategori_line_edit.text()
        fiyat = self.duzenlesayfa.fiyat_line_Edit.text()
        eklendigi_tarih = self.duzenlesayfa.eklendigi_tarih_line_edit.text()


        if _id.strip() == "":
            QMessageBox.warning(self,"Uyarı","ID kısmı boş bırakılamaz!")
        else:
            self.listeSinyali.emit()
            veriler = self.dveritabani._Guncelle(_id, kitap_adi, yazar_adi, sayfa_sayisi, kategori,fiyat, eklendigi_tarih)




        if veriler:
            self.listeSinyali.emit()
            QMessageBox.information(self, 'Başarılı', 'Kayıt başarıyla güncellendi.')
        else:
            QMessageBox.warning(self, 'Hata', 'Kayıt güncellenirken bir hata oluştu.')



    
    

        



    