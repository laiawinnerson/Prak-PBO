from abc import ABC, abstractclassmethod

import datetime

class AkunBank(ABC):
    def __init__(self, nama, tahun_daftar, saldo) -> None:
        self.nama = nama
        self.tahun_daftar = tahun_daftar
        self.saldo = saldo

    def lihat_saldo(self):
        pass

    @abstractclassmethod
    def transfer_saldo(self):
        pass

    @abstractclassmethod
    def lihat_suku_bunga(self):
        pass


class AkunGold(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo) -> None:
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, saldo_transfer):
        biaya_admin = 0

        if saldo_transfer >= 100000 :
            if datetime.datetime.now().year - self.tahun_daftar < 3 :
                biaya_admin = 2000
            
        self.saldo = self.saldo - saldo_transfer - biaya_admin

    def lihat_suku_bunga(self):
        if self.saldo >= 1000000000 :
            if datetime.datetime.now().year - self.tahun_daftar < 3 :
                self.bunga = 0.01
            else :
                self.bunga = 0.02
        else :
            self.bunga = 0.02

        return f"{self.bunga:%}"


class AkunSilver(AkunBank):
    def __init__(self, nama, tahun_daftar, saldo) -> None:
        super().__init__(nama, tahun_daftar, saldo)

    def transfer_saldo(self, saldo_transfer):
        biaya_admin = 0

        if saldo_transfer >= 100000 :
            if datetime.datetime.now().year - self.tahun_daftar < 3 :
                biaya_admin = 5000
            else :
                biaya_admin = 2000
            
        self.saldo = self.saldo - saldo_transfer - biaya_admin

    def lihat_suku_bunga(self):
        if self.saldo >= 10000000 :
            if datetime.datetime.now().year - self.tahun_daftar < 3 :
                self.bunga = 0.01
            else :
                self.bunga = 0.02
        else :
            self.bunga = 0.02

        return f"{self.bunga:%}"
    

akungold = AkunGold("winner", 2003, 1000000)

akungold.transfer_saldo(100000)

print(akungold.nama)
print(akungold.saldo)
print(akungold.tahun_daftar)
print(akungold.lihat_suku_bunga())




