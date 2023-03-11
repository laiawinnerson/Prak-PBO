class Manusia_Sekolah :
    # Class Manusia_Sekolah merupakan class induk
    # yang menggambarkan seorang manusia yang berada
    # di lingkungan sekolah dan memiliki nama serta umur

    _jumlah_manusia  = 0
    _jumlah_guru = 0
    _jumlah_siswa = 0

    # jumlah_manusia, jumlah_guru, dan jumlah_siswa
    # bersifat protected agar hanya dapat diakses dari
    # internal class atau sub class.

    def __init__(self, nama, umur):
        self.__nama  = nama
        self.__umur =  umur
        Manusia_Sekolah._jumlah_manusia += 1

    # atribut objek nama dan umur bersifat privat
    # agar menghindari pengubahan nama dan umur yang
    # tidak disengaja

    def get_nama(self) :
        return self.__nama

    def get_umur (self) :
        return self.__umur
    
    def get_jumlah_manusia():
        return Manusia_Sekolah._jumlah_manusia
    
    def get_jumlah_guru():
        return Manusia_Sekolah._jumlah_guru
    
    def get_jumlah_siswa():
        return Manusia_Sekolah._jumlah_siswa

class Guru(Manusia_Sekolah) :
    # Class Guru merupakan class yang menggambarkan
    # seorang guru yang memiliki nama, umur, dan
    # pelajaran yang diampuh.

    # Class Guru merupakan kelas turunan dari
    # class Manusia_Sekolah.

    def __init__(self, nama, umur, pelajaran_yang_diampuh):
        super().__init__(nama, umur)
        self.__pelajaran_yang_diampuh = pelajaran_yang_diampuh
        Manusia_Sekolah._jumlah_guru += 1

    # atribut objek nama, umur, dan pelajaran yang diampuh 
    # bersifat privat agar menghindari pengubahan nama, umur
    # dan pelajaran yang diampuh yang tidak disengaja

    def __del__(self) :
        Manusia_Sekolah._jumlah_manusia -= 1
        Manusia_Sekolah._jumlah_guru -= 1

    # Jika objek guru dihapus akan mengurangi 1
    # jumlah manusia dan mengurangi 1 jumlah guru

    # Objek dihapus bila seorang guru tidak bekerja
    # lagi di sekolah

    def get_pelajaran_yang_diampu(self):
        return self.__pelajaran_yang_diampuh
    
    def berhenti_menjadi_guru(self) :
        print(f"Guru bernama {self.get_nama()} telah berhenti sebagi guru")
        self.__del__()

class Siswa(Manusia_Sekolah) :

    # Class Siswa merupakan class yang menggambarkan
    # seorang siswa yang memiliki nama, umur, dan
    # kelas yang ia tempati.

    # Class Siswa merupakan kelas turunan dari
    # class Manusia_Sekolah.

    def __init__(self, nama, umur, kelas):
        super().__init__(nama, umur)
        self.__kelas = kelas
        Manusia_Sekolah._jumlah_siswa += 1
    
    # atribut objek nama, umur, dan kelas bersifat 
    # privat agar menghindari pengubahan nama, umur
    # dan kelas yang diampuh yang tidak disengaja

    def __del__(self) :
        
        Manusia_Sekolah._jumlah_manusia -= 1
        Manusia_Sekolah._jumlah_siswa -= 1
        pass

    # Jika objek siswa dihapus akan mengurangi 1
    # jumlah manusia dan mengurangi 1 jumlah siswa

    # Objek siswa dihapus bila seorang siswa 
    # keluar/berhenti dari sekolah


    def get_kelas(self) :
        return self.__kelas
    
    def telah_lulus(self):
        print(f"Siswa bernama {self.get_nama()} telah berhenti lulus")
        self.__del__()
    


# conton penggunaan class

guru1 = Guru("Siti", 25, "Matematika")
guru2 = Guru("Budi", 26, "Fisika")
siswa1 = Siswa("Harun", 17, "12-IPA-1")
siswa2 = Siswa("Bunga", 16, "11-IPA-1")

print(f"Jumlah manusia  : {Manusia_Sekolah.get_jumlah_manusia()}")
print(f"Jumlah guru     : {Manusia_Sekolah.get_jumlah_guru()}")
print(f"Jumlah siswa    : {Manusia_Sekolah.get_jumlah_siswa()}")

print("")
guru1.berhenti_menjadi_guru()
siswa1.telah_lulus()
print("")


print(f"Jumlah manusia  : {Manusia_Sekolah.get_jumlah_manusia()}")
print(f"Jumlah guru     : {Manusia_Sekolah.get_jumlah_guru()}")
print(f"Jumlah siswa    : {Manusia_Sekolah.get_jumlah_siswa()}")