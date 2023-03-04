class Mahasiswa :
    def __init__(self, nim:int, nama:str, kelas_pbo_siakad:str, jumlah_sks:int) -> None:
        self.__nim = nim
        self.__nama = nama
        self.__kelas_pbo_siakad = kelas_pbo_siakad
        self.__jumlah_sks = jumlah_sks

    def tampilkan_data(self) :
        print("Data Mahasiswa : ")
        print(f"Nim                 : {self.__nim}")
        print(f"Nama                : {self.__nama}")
        print(f"Kelas PBO Siakad    : {self.__kelas_pbo_siakad}")
        print(f"Jumlah sks          : {self.__jumlah_sks} \n")
    
    def tukar_kelas_pbo_siakad(self, kelas_pbo_tujuan : str):
        self.__kelas_pbo_siakad = kelas_pbo_tujuan
        

mahasiswa_1 = Mahasiswa(121140121, "Winnerson Laia", "RC", 20)

mahasiswa_1.tampilkan_data()

mahasiswa_1.tukar_kelas_pbo_siakad("RB")

mahasiswa_1.tampilkan_data()
