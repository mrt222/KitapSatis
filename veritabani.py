import sqlite3 
import os 

class veritabani():
    def __init__(self):
        dizin_yol = os.path.dirname(os.path.abspath(__file__))
        self.db = os.path.join(dizin_yol,'kutuphane.db')
        print(self.db)
        

    def vtac(self):
        self.conn = sqlite3.connect(self.db)
        self.cursor = self.conn.cursor()


    def vtkapat(self):
        self.cursor.close()

    
    def kayitEkle(self,_id,kitap_adi,yazar_adi,sayfa_sayisi,kategori,kitap_fiyati,eklendigi_tarih):
       try:
        self.vtac()
        sql = "insert into kutuphane (id, kitap_adi,yazar_Adi,sayfa_sayisi,kategori,kitap_fiyati,eklendigi_tarih) values (?,?,?,?,?,?,?)"
        self.cursor.execute(sql,(_id,kitap_adi,yazar_adi,sayfa_sayisi,kategori,kitap_fiyati,eklendigi_tarih))
        self.conn.commit()
        return True
       except:
          return False
       finally:
          self.vtkapat()


    def kayitGoster(self):
       try:
          self.vtac()
          sql = "select * from kutuphane order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat



    def _Guncelle(self,_id,kitap_adi,yazar_adi,sayfa_sayisi,kategori,kitap_fiyati,eklendigi_tarih):
     try:
        self.vtac()
        sql = "UPDATE kutuphane SET kitap_adi = ?, yazar_Adi = ?, sayfa_sayisi = ?, kategori = ?,kitap_fiyati = ?, eklendigi_tarih = ? WHERE id = ?"
        self.cursor.execute(sql, (kitap_adi,yazar_adi,sayfa_sayisi,kategori,kitap_fiyati,eklendigi_tarih ,_id))
        self.conn.commit()
        return True
     except:
        return False
     finally:
        self.vtkapat()   


    def sil(self, _id):
       try:
          self.vtac()
          sql = "DELETE FROM kutuphane WHERE id = ?"
          self.cursor.execute(sql, (_id,))
          self.conn.commit()
          return True
       except sqlite3.Error as e:
          print("SQLite Hatası:", e) 
          return False
       finally:
        self.vtkapat()
          
    


    def ara(self,kitap_adi):
       try:
        self.vtac()
        sql = "SELECT * FROM kutuphane WHERE `kitap_adi` LIKE '%" + kitap_adi + "%' ORDER BY ID DESC"
        self.cursor.execute(sql)
        veriler = self.cursor.fetchall()
        return veriler
       except Exception as e:
        print("Arama hatası:", e)
        return False
       finally:
        self.vtkapat()




    def SatinAl(self, _id, kitap_adi, ad_soyad, adres, fiyat):
       try:
        self.vtac()
        sql = "INSERT INTO satis (id, kitap_adi, ad_soyad, adres, fiyat) VALUES (?, ?, ?, ?, ?)"
        self.cursor.execute(sql, (_id, kitap_adi, ad_soyad, adres, fiyat))
        self.conn.commit()
        return True
       except Exception as e:
        print(f"Hata oluştu: {e}")
        return False
       finally:
        self.vtkapat()



    def KitapkayitGoster(self):
       try:
          self.vtac()
          sql = "select * from satis order by id "
          self.cursor.execute(sql)
          veriler = self.cursor.fetchall()
          return veriler
       except:
          return False
       finally:
          self.vtkapat




    def MusteriAra(self,ad_soyad):
       try:
        self.vtac()
        sql = "SELECT * FROM satis WHERE `ad_soyad` LIKE '%" + ad_soyad + "%' ORDER BY ID DESC"
        self.cursor.execute(sql)
        veriler = self.cursor.fetchall()
        return veriler
       except Exception as e:
        print("Arama hatası:", e)
        return False
       finally:
        self.vtkapat()


    