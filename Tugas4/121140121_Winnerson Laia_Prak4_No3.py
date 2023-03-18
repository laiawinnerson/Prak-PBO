# ini merupakan salah salah satu implementasi
# dari inheritance.

# Progam ini memiliki dua class, yakni :
# 1. class Vektor2D sebagi class induk
# 2. Class Vektor3D yang merupakan class turunan dari class Vektor2D

# Class Vektor2D merupakan class yang mewakili
# objek vektor 2 dimensi, yang dimana vektor memiliki
# nilai x, y. Selain itu terdapat beberapa
# operasi pada vektor 2 dimensi yaitu penambahan 2 matriks,
# pengurangan 2 matriks, perkalian matriks dengan konstanta.

# Class Vektor3D merupakan class yang mewakili
# objek vektor 3-dimensi, yang dimana vektor memiliki
# nilai x, y, dan z. Selain itu terdapat beberapa
# operasi pada vektor 3-dimensi yaitu penambahan 2 matriks,
# pengurangan 2 matriks, perkalian matriks dengan konstanta.


class Vektor2D :
    def __init__(self, x:float, y:float) -> None:
        self.x = x
        self.y = y
    
    # perkalian matriks dan konstanta
    def __mul__(self, konstanta) :
        x_baru = self.x * konstanta
        y_baru = self.y * konstanta
        return Vektor2D(x_baru, y_baru)
    
    # pembagian matriks dengan pembagi
    def __truediv__(self, pembagi):
        x_baru = self.x / pembagi
        y_baru = self.y / pembagi
        return Vektor2D(x_baru, y_baru)
    
    # pejumlahan antara 2 vektor 2-dimensi
    def __add__(self, vektor2Dlain) :
        x_baru = self.x + vektor2Dlain.x
        y_baru = self.y + vektor2Dlain.y
        return Vektor2D(x_baru, y_baru)
    
    # pengurangan antara 2 vektor 2-dimensi
    def __sub__(self, vektor2Dlain) : 
        x_baru = self.x - vektor2Dlain.x
        y_baru = self.y - vektor2Dlain.y
        return Vektor2D(x_baru, y_baru)

    # menampilkan informasi tentang vektor 2-dimensi
    def __str__(self) -> str:
        return "x: " + str(self.x) + ",y: " + str(self.y)

class Vektor3D(Vektor2D):
    def __init__(self, x:float, y:float, z:float) -> None:
        super().__init__(x, y)
        self.z = z

    # perkalian matriks dan konstanta
    def __mul__(self, konstanta):
        x_baru = self.x * konstanta
        y_baru = self.y * konstanta
        z_baru = self.z * konstanta
        return Vektor2D(x_baru, y_baru, z_baru)
    
    # pembagian matriks dengan pembagi
    def __truediv__(self, pembagi) :
        x_baru = self.x / pembagi
        y_baru = self.y / pembagi
        z_baru = self.z / pembagi
        return Vektor3D(x_baru, y_baru, z_baru)
    
    # pejumlahan antara 2 vektor 3-dimensi
    def __add__(self, vektor3Dlain) :
        x_baru = self.x + vektor3Dlain.x
        y_baru = self.y + vektor3Dlain.y
        z_baru = self.z + vektor3Dlain.z
        return Vektor3D(x_baru, y_baru, z_baru)
    
    # pengurangan antara 2 vektor 3-dimensi
    def __sub__(self, vektor3Dlain) : 
        x_baru = self.x - vektor3Dlain.x
        y_baru = self.y - vektor3Dlain.y
        z_baru = self.z - vektor3Dlain.z
        return Vektor3D(x_baru, y_baru, z_baru)
    
    # menampilkan informasi tentang vektor 3-dimensi
    def __str__(self) -> str:
        return super().__str__() +  ",z:" + str(self.z)



x1 = Vektor2D(2,2)
x2 = x1 * 2

print(x1)
print(x2)


