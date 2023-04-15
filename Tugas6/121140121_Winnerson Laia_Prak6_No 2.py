from abc import ABC, abstractclassmethod

class DBMS(ABC):
    @abstractclassmethod
    def lihat_tabel(self):
        pass

    @abstractclassmethod
    def tambah_data(self):
        pass

    @abstractclassmethod
    def hapus_tabel(self):
        pass

class MySQL(DBMS) :
    def __init__(self, nama_tabel) -> None:
        self.nama_tabel = nama_tabel

    def lihat_tabel(self):
        print(f"SELECT * FROM {self.nama_tabel}")

    def tambah_data(self, nama_kolom, nilai):
        print(f"INSERT INTO {self.nama_tabel} ({nama_kolom}) VALUES ({nilai}")

    def hapus_tabel(self) :
        print(f"DROP TABLE {self.nama_tabel}") 

class MongoDB(DBMS) :
    def __init__(self, nama_tabel) -> None:
        self.nama_tabel = nama_tabel

    def lihat_tabel(self):
        print(f"db.{self.nama_tabel}.find()")

    def tambah_data(self, nama_kolom, nilai):
        print(f"""db.{self.nama_tabel}.insertOne({{{nama_kolom}}}:"{nilai}")""")

    def hapus_tabel(self) :
        print(f"db.{self.nama_tabel}.drop()")        

