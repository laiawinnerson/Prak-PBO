username = "informatika"
password = "12345678"


for i in range(3) :
    input_username = input("Username anda : ")
    input_password = input("Password anda : ")

    if input_username == username and input_password == password :
        print("Berhasil login!")
        break
    else :
        if i == 2 :
            print("Akun terblokir")
        else:
            print("Username atau password salah coba lagi")
