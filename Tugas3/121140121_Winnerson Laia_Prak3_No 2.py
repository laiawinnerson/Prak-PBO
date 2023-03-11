class AkunBank :
    list_pelanggan = []

    def __init__(self, no_pelanggan : int, nama_pelanggan : str , jumlah_saldo:int) -> None:
        self.__no_pelanggan =  no_pelanggan
        self.__nama_pelanggan = nama_pelanggan
        self.__jumlah_saldo = jumlah_saldo

        AkunBank.list_pelanggan.append(self)

    def get_no_pelanggan(self) :
        return self.__no_pelanggan

    def get_nama(self) :
        return self.__nama_pelanggan
    
    def mendapat_saldo(self, jumlah_saldo:int) :
        self.__jumlah_saldo += jumlah_saldo
        pass

    def lihat_saldo(self) :
        print("")
        print(f"{self.__nama_pelanggan} memiliki saldo Rp {self.__jumlah_saldo}")
        print("")

    def tarik_tunai(self) :
        print("")
        tarik = int(input("Masukkan jumlah nominal yang ingin ditarik : "))
        if tarik <= self.__jumlah_saldo :
            self.__jumlah_saldo -= tarik
            print("Pesan : saldo berhasil ditarik")
        else :
            print("Pesan : nominal saldo yang anda Anda punya tidak cukup !")
        print("")

    def transfer(self) :
        print("")
        transfer = int(input("Masukkan nominal yang ingin ditransfer : "))
        nomor_rekening_tujuan = int(input("Masukkan nomor rekening tujuan : "))

        nomor_rekening_ada  = False

        if nomor_rekening_tujuan != self.__no_pelanggan :
            for akun in AkunBank.list_pelanggan :
                if akun.get_no_pelanggan() == nomor_rekening_tujuan :
                    nomor_rekening_ada = True
                
                    if nomor_rekening_ada :
                        print(f"Pesan : transfer Rp {transfer} ke {akun.get_nama()} sukses !")
                        self.__jumlah_saldo -= transfer
                        akun.mendapat_saldo(transfer)
                        break
            if nomor_rekening_ada == False  : 
                print("Pesan : nomor rekening tujuan tidak dikenali! Kembali ke menu utama...")

        else :
            print("Pesan : anda tidak dapat mentransfer saldo ke rekening sendiri !")

        print("")

    def lihat_menu(self) :
        ulangi = True
        
        while ulangi :
            print("Selamat datang di Bank Kami")
            print("Halo nasabah, ingin melakukan apa ?")
            print("1. Lihat saldo")
            print("2. Tarik tunai")
            print("3. Transfer saldo")
            print("4. Keluar")

            pilihan = int(input("Masukkan nomor input : "))

            if pilihan == 1 :
                self.lihat_saldo()
            elif pilihan == 2 :
                self.tarik_tunai()
            elif pilihan == 3 :
                self.transfer()
            elif pilihan == 4 :
                ulangi = False
            else:
                print("\nPesan : pilihan tersebut tidak tersedia!\n")


# penggunaan

Akun1 = AkunBank(1234, "Winner", 5000000000)
Akun2 = AkunBank(2345, "Ukraina", 6666666666)
Akun3 = AkunBank(3456, "Elon Musk", 9999999999)


Akun1.lihat_menu()

