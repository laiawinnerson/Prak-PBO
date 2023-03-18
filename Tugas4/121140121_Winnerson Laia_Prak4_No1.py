class Komputer :
    def __init__(self, merk, nama, harga) -> None:
        self.nama = nama
        self.harga = harga
        self.merk = merk

    def __str__(self) -> str:
        return f" {self.nama} produksi {self.merk}"


class Processor(Komputer):
    def __init__(self, merk, nama, harga, jumlah_core, kecepatan_processor) -> None:
        super().__init__(merk, nama, harga)
        self.jumlah_core = jumlah_core
        self.kecepatan_processor = kecepatan_processor

    def __str__(self) -> str:
        return "Processor" + super().__str__()

class RAM(Komputer): 
    def __init__(self, merk, nama, harga, kapasitas) -> None:
        super().__init__(merk, nama, harga)
        self.kapasitas = kapasitas

    def __str__(self) -> str:
        return "RAM" + super().__str__()

class HDD(Komputer): 
    def __init__(self, merk, nama, harga, kapasitas, rpm) -> None:
        super().__init__(merk, nama, harga)
        self.kapasitas = kapasitas
        self.rpm = rpm

    def __str__(self) -> str:
        return "HDD" + super().__str__()


class VGA(Komputer): 
    def __init__(self, merk, nama, harga, kapasitas) -> None:
        super().__init__(merk, nama, harga)
        self.kapasitas = kapasitas

    def __str__(self) -> str:
        return "VGA" + super().__str__()


class PSU(Komputer): 
    def __init__(self, merk, nama, harga, daya) -> None:
        super().__init__(merk, nama, harga)
        self.daya = daya

    def __str__(self) -> str:
        return "PSU" + super().__str__()


p1 = Processor('Intel','Core i7 7740X', 4350000 , 4, '4.3GHz')
p2 = Processor('AMD','Ryzen 5 3600', 250000,4 , '4.3GHz')
ram1 = RAM('V-Gen','DDR4 SODimm PC19200/2400MHz',328000,'4GB')
ram2 = RAM('G.SKILL','DDR4 2400MHz',328000,'4GB')
hdd1 = HDD('Seagate','HDD 2.5 inch',295000,'500GB',7200)
hdd2 = HDD('Seagate','HDD 2.5 inch',295000,'1000GB',7200)
vga1 = VGA('Asus','VGA GTX 1050',250000,'2GB')
vga2 = VGA('Asus','1060Ti',250000,'8GB')
psu1 = PSU('Corsair','Corsair V550',250000,'500W')
psu2 = PSU('Corsair','Corsair V550',250000,'500W')


rakit = [[p1,ram1,hdd1,vga1,psu1],[p2,ram2,hdd2,vga2,psu2]]

for pc in rakit : 
    i = 1 
    print("Komputer ", i)
    for komponen in pc :
        print(komponen)
    print("")

