class Robot:
    jumlah_turn = 0
    hasil_suit = 0

    def __init__(self, nama, health, damage) -> None:
        self.nama = nama
        self.health = health
        self.damage = damage
        self.tangan_robot = 0
        self.power_upgrade = False
        self.robotku = False

    def set_tangan_robot(self, tangan_robot) :
        self.tangan_robot = tangan_robot

    def lakukan_aksi(self, objek_tujuan):
        objek_tujuan.health -= self.damage

    def power_up(self) :
        pass

    def power_down(self) :
        pass

    def jumlah_turn_bertambah() :
        Robot.jumlah_turn += 1
    
    def set_robotku(objek):
        objek.robotku = True
        pass

    def Suit(objek_1, objek_2):
        tgn_rbt_1 = objek_1.tangan_robot
        tgn_rbt_2 = objek_2.tangan_robot

        if tgn_rbt_1 == tgn_rbt_2 :
            print("Tidak ada yang menang suit")
        else :
            if tgn_rbt_1 == 1 :
                if tgn_rbt_2 == 2 :
                    Robot.hasil_suit = 2
                elif tgn_rbt_2 == 3 :
                    Robot.hasil_suit = 1
            elif tgn_rbt_1 == 2 :
                if tgn_rbt_2 == 3 :
                    Robot.hasil_suit = 2
                elif tgn_rbt_2 == 1 :
                    Robot.hasil_suit = 1
            elif tgn_rbt_1 == 3 :
                if tgn_rbt_2 == 1 :
                    Robot.hasil_suit = 2
                elif tgn_rbt_2 == 2 :
                    Robot.hasil_suit = 1

        if Robot.hasil_suit == 1 :
            objek_1.power_up()
            objek_1.lakukan_aksi(objek_2)
            objek_1.power_down()
        elif Robot.hasil_suit == 2 :
            objek_2.power_up()
            objek_2.lakukan_aksi(objek_1)
            objek_2.power_down()
        
        objek_1.tangan_robot = 0
        objek_2.tangan_robot = 0

        Robot.hasil_suit = 0

class Antares(Robot) :
    def __init__(self, nama  = "Antares", health = 50000, damage = 5000) -> None:
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 3 == 0 and Robot.jumlah_turn > 1 :
            self.damage *= 1.5
            self.power_upgrade = True

        if self.robotku ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")
        
    def power_down(self) :
        if self.power_upgrade == True :
            self.damage /= 1.5
        self.power_upgrade = False

class Alphasetia(Robot) :
    def __init__(self, nama = "Alphasetia", health = 40000, damage = 6000) -> None:
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 2 == 0 and Robot.jumlah_turn > 1 :
            self.health += 4000
            if self.robotku ==  True :
                print(f"Robotmu ({self.nama}) menambah darah sebanyak 4000 HP")
            else :
                print(f"Robot lawan ({self.nama}) menambah darah sebanyak 4000 HP")

        if self.robotku ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")
                
class Lecalicus(Robot) :
    def __init__(self, nama = "Lecalicus", health = 450000, damage = 5500) -> None:
        super().__init__(nama, health, damage)

    def power_up(self):
        if Robot.jumlah_turn % 4 == 0 and Robot.jumlah_turn > 1 :
            self.damage *= 2
            self.health += 7000
            self.power_upgrade = True
            if self.robotku ==  True :
                print(f"Robotmu ({self.nama}) menambah darah sebanyak 7000 HP")
            else :
                print(f"Robot lawan ({self.nama}) menambah darah sebanyak 7000 HP")

        if self.robotku ==  True :
            print(f"Robotmu ({self.nama}) menyerang sebanyak {self.damage} DMG")
        else :
            print(f"Robot lawan ({self.nama}) menyerang sebanyak {self.damage} DMG")

    def power_down(self) :
        if self.power_upgrade == True :
            self.damage /= 2
        self.power_upgrade = False


# Main Program
print("Selamat datang di pertandingan robot Yamako")
pil_robotku = int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))
pil_robot_lawan= int(input("Pilih robotmu (1 = Antares, 2 = Alphasetia, 3 = Lecalicus): "))

if pil_robotku == 1 :
    robotku = Antares()
elif pil_robotku == 2 :
    robotku = Alphasetia()
elif pil_robotku == 3 :
    robotku = Lecalicus()

Robot.set_robotku(robotku)

if pil_robot_lawan == 1 :
    robotlawan = Antares()
elif pil_robot_lawan == 2 :
    robotlawan = Alphasetia()
elif pil_robot_lawan == 3 :
    robotlawan = Lecalicus()

print("Selanjutnya, pilih 1 untuk batu, 2 untuk kertas, dan 3 untuk gunting", "\n")

while robotku.health > 0 and robotlawan.health > 0 :
    Robot.jumlah_turn_bertambah()
    print(f"Turn saat ini : {Robot.jumlah_turn}")
    print(f"Robotmu ({robotku.nama} - {robotku.health}), robot lawan ({robotlawan.nama} - {robotlawan.health}")

    tangan_robotku = int(input(f"Pilih tangan robotmu ({robotku.nama}): "))
    tangan_robotlawan = int(input(f"Pilih tangan robotmu ({robotlawan.nama}): "))

    robotku.set_tangan_robot(tangan_robotku)
    robotlawan.set_tangan_robot(tangan_robotlawan)

    Robot.Suit(robotku, robotlawan)

    print("")