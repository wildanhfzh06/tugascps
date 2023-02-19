class HitungGeometri:
    def _init_(self,nama,nim,kelas):
        self.nama=nama
        self.nim=nim
        self.kelas=kelas
    def info(self):
        print("Nama: ",self.nama)
        print("NIM: ",self.nim)
        print("Kelas: ",self.kelas)
        
class Persegi(HitungGeometri):
    def _init_(sisi):
        self.sisi=sisi
    def keliling(sisi):
        print(sisi*4)
    def luas(sisi):
        print(sisi*sisi)

class Lingkaran(HitungGeometri):
    def _init_(jari):
        self.jari=jari
    def keliling(jari):
        print(2*3.14*jari)
    def luas(jari):
        print(3.14*jari*jari)

    
class Segitiga(HitungGeometri):
    def _init_(alas, tinggi, sisi):
        self.alas=alas
        self.tinggi=tinggi
        self.sisi1=sisi1
        self.sisi2=sisi2
        self.sisi3=sisi3
    def keliling(sisi1, sisi2, sisi3):
        print(sisi1 + sisi2 + sisi3)
    def luas(alas, tinggi):
        print(alas*tinggi/2)

class PersegiPanjang(HitungGeometri):
    def _init_(panjang, lebar):
        self.panjang=panjang
        self.lebar=lebar
    def keliling(panjang, lebar):
        print(2*(panjang+lebar))
    def luas(panjang, lebar):
        print(panjang*lebar)

    
class JajaranGenjang(HitungGeometri):
    def _init_(alas, tinggi, sisimiring):
        self.alas=alas
        self.tinggi=tinggi
        self.sisimiring=sisimiring
    def keliling(alas, sisimiring):
        print(2*(alas + sisimiring)
    def luas(alas, tinggi):
        print(alas*tinggi)

    
class BelahKetupat(HitungGeometri):
    def _init_(d1, d2, sisi):
        self.d1=d1
        self.d2=d2
        self.sisi=sisi
    def keliling(sisi):
        print(4*sisi)
    def luas(d1, d2):
        print(d1*d2/2)

    
class Trapesium(HitungGeometri):
    def _init_(sisiatas, sisibawah, sisimiring, tinggi):
        self.sisiatas=sisiatas
        self.tinggi=tinggi
        self.sisibawah=sisibawah
        self.sisimiring=sisimiring
    def keliling(sisiatas, sisibawah, sisimiring, tinggi):
        print(sisiatas + sisibawah + sisimiring + tinggi)
    def luas(sisiatas, sisibawah, tinggi):
        print((sisiatas + sisibawah)*t/2)


class BelahKetupat(HitungGeometri):
    def _init_(d1, d2, sisi1, sisi2):
        self.d1=d1
        self.d2=d2
        self.sisi1=sisi1
        self.sisi2=sisi2
    def keliling(sisi1, sisi2):
        print(2*(sisi1 + sisi2)
    def luas(d1, d2):
        print(d1*d2/2)

obj1 = HitungGeometri("Muhammad Wildan Hafizh", 1101213287, "TT-45-09")
obj1.info()
