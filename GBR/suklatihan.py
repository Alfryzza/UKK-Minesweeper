from abc import ABC, abstractmethod

class Kendaraan(ABC):
    def __init__(self, nama, bbm):
        self.nama = nama
        self.bbm = bbm
    
    @abstractmethod
    def bergerak(self, jarak):
        pass

class Mobil(Kendaraan):
    def bergerak(self, jarak):
        penggunaan = jarak * 0.2
        self.bbm -= penggunaan
        print(f"{self.nama} berjalan sejauh {jarak} km")
        print(f"Sisa BBM: {self.bbm} liter")


class Motor(Kendaraan):
    def bergerak(self, jarak):
        penggunaan = jarak * 0.1
        self.bbm -= penggunaan
        print(f"{self.nama} berjalan sejauh {jarak} km")
        print(f"Sisa BBM: {self.bbm} liter")


class Pesawat(Kendaraan):
    def bergerak(self, jarak):  
        penggunaan = jarak * 1.5
        self.bbm -= penggunaan
        print(f"{self.nama} terbang sejauh {jarak} km")
        print(f"Sisa BBM: {self.bbm} liter")

        
        
class BBM:
    def __init__(self, liter):
        self.liter = liter

    def __add__(self, other):
        return self.liter + other.liter  

    def __str__(self):
        return f"BBM: {self.liter}"



def jalankan(k):
    k.bergerak(10)

m = Mobil("Avanza", 50)
mt = Motor("Ninja", 20)
p = Pesawat("PESAWAt", 100)

for k in [m, mt, p]:
    jalankan(k)