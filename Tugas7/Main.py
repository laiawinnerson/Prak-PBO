import time
import threading
from tkinter import *
from playsound import playsound

class Pomodoro(Frame):
    def __init__(self, master):
        super().__init__(master = master)
        self.running = False
        self.stop = False
        self.keluar = False
        self.pomodoro = True
        self.state = "Pomodoro"
        self.durasi_pomodoro = 25*60
        self.durasi_berhenti = 5*60
        self.sisa_waktu = self.durasi_pomodoro
        self.reset = False

        self.frame = Frame(master= self)
        self.frame.pack(expand= True)

        self.frame1 = Frame(master= self.frame, width= 350, height= 200, bg="#1A1A2E")
        self.frame1.pack(fill="both")
        self.frame2 = Frame(master= self.frame)
        self.frame2.pack(fill="both")
        self.frame3 = Frame(master= self.frame, width= 350, height= 85, bg="#1A1A2E")
        self.frame3.pack(fill="both")

        menit = self.sisa_waktu // 60
        detik = self.sisa_waktu % 60

        self.label_sisa_waktu = Label(master= self.frame1, 
                                      text= f"{menit:02d}:{detik:02d}",  
                                      font= "Arial, 30", bg="#1A1A2E", fg = "white")
        self.label_sisa_waktu.pack(pady= 10)

        self.label_state = Label(master=self.frame1, text= self.state, font= "Arial, 14", bg="#1A1A2E", fg = "white")
        self.label_state.pack(pady= 5)

        self.framemulai = Frame(master= self.frame2, bg="#1A1A2E")
        self.framemulai.pack(fill= "both", side= "left", expand= True)

        self.framestop = Frame(master= self.frame2,bg="#1A1A2E")
        self.framestop.pack(fill= "both", side= "left", expand= True)

        self.framereset = Frame(master= self.frame2,bg="#1A1A2E")
        self.framereset.pack(fill= "both", side= "left", expand= True)

        self.tombol_mulai = Button(master= self.framemulai, 
                                   text= "Mulai", command= self.lakukan_mulai_thread, 
                                   relief="flat", bg = "darkslateblue" , fg = "white", 
                                   highlightbackground= "darkslateblue", 
                                   activebackground= "darkslateblue", 
                                   activeforeground= "white")
        self.tombol_mulai.pack(padx = 20, pady= 10, expand= True)

        self.tombol_stop = Button(master= self.framestop, 
                                  text= "Stop", 
                                  command= self.lakukan_stop, 
                                  relief="flat", bg = "darkslateblue" , fg = "white", 
                                  highlightbackground= "darkslateblue", 
                                  activebackground= "darkslateblue", 
                                  activeforeground= "white")
        self.tombol_stop.pack(padx = 20, pady= 10, expand= True)

        self.tombol_reset = Button(master= self.framereset, 
                                   text= "Reset", 
                                   command=self.lakukan_reset, 
                                   relief="flat", bg = "darkslateblue" , fg = "white", 
                                   highlightbackground= "darkslateblue", 
                                   activebackground= "darkslateblue", 
                                   activeforeground= "white")
        
        self.tombol_reset.pack(padx = 20, pady= 10, expand= True)

        self.label_pomodoro = Label(master= self.frame3, text= "Durasi pomodoro",bg="#1A1A2E", fg = "white")
        self.label_pomodoro.place(x = 10,  y = 10)

        self.label_berhenti = Label(master= self.frame3, text= "Durasi berhenti",bg="#1A1A2E", fg = "white")
        self.label_berhenti.place(x = 10,  y = 50)

        self.entry_durasi_pomodoro = Entry(master=self.frame3, width= 10, relief= "flat")
        self.entry_durasi_pomodoro.place(x= 130, y = 10)

        self.entry_durasi_berhenti = Entry(master=self.frame3, width= 10, relief= "flat")
        self.entry_durasi_berhenti.place(x= 130, y = 50)

        self.tombol_terapkan = Button(master= self.frame3, 
                                      text= "Terapkan", 
                                      command= self.lakukan_terapkan, 
                                      relief="flat", bg = "darkslateblue" , fg = "white", 
                                      highlightbackground= "darkslateblue", 
                                      activebackground= "darkslateblue", 
                                      activeforeground= "white")
        self.tombol_terapkan.place(x = 240, y = 20)

    def suara_ting(self):
        playsound('suara_ting.ogg')
    
    def mulai(self):
        while self.stop != True and self.sisa_waktu > 0:
            if self.reset:
                self.sisa_waktu = self.durasi_pomodoro
                menit = self.durasi_pomodoro // 60
                detik = self.durasi_pomodoro % 60
                self.label_sisa_waktu.config(text= f"{menit:02d}:{detik:02d}")
                self.label_state.config(text = "Pomodoro")
                self.reset = False
                self.pomodoro = True

            if self.pomodoro:
                menit = self.sisa_waktu // 60
                detik = self.sisa_waktu % 60
                self.label_sisa_waktu.config(text= f"{menit:02d}:{detik:02d}")
                time.sleep(1)
                self.sisa_waktu -= 1
            else :
                menit = self.sisa_waktu // 60
                detik = self.sisa_waktu % 60
                self.label_sisa_waktu.config(text= f"{menit:02d}:{detik:02d}")
                time.sleep(1)
                self.sisa_waktu -= 1
            if self.keluar:
                break
        
        if self.pomodoro and self.stop!= True and self.keluar != True:
            t2 = threading.Thread(target=self.suara_ting)
            t2.start()
            self.pomodoro = False
            self.label_state.config(text= "Istrahat")
            self.sisa_waktu = self.durasi_berhenti
            self.mulai()
        elif self.pomodoro != True and self.stop != True and self.keluar!= True:
            t2 = threading.Thread(target=self.suara_ting)
            t2.start()
            self.pomodoro = True
            self.label_state.config(text= "Pomodoro")
            self.sisa_waktu = self.durasi_pomodoro
            self.mulai()

    def lakukan_mulai_thread(self):
        if self.stop:
            self.stop = False

        if self.running != True:
            t = threading.Thread(target= self.mulai)
            t.start()
            self.running = True
        pass
    
    def lakukan_stop(self):
        self.stop = True
        self.running = False
    
    def lakukan_reset(self):
        self.stop = True
        self.running = False
        self.reset = True

        self.sisa_waktu = self.durasi_pomodoro
        menit = self.sisa_waktu // 60
        detik = self.sisa_waktu % 60
        self.label_sisa_waktu.config(text= f"{menit:02d}:{detik:02d}")
    
    def lakukan_terapkan(self):
        self.stop = True
        self.running = False
        self.reset = True

        try :
            self.durasi_pomodoro = int(self.entry_durasi_pomodoro.get()) * 60
        except :
            self.entry_durasi_pomodoro.delete(0, END)
            self.entry_durasi_pomodoro.insert(0, "nilai tdk bnr!")
            try :
                self.durasi_berhenti = int(self.entry_durasi_berhenti.get()) * 60
            except :
                self.entry_durasi_berhenti.delete(0, END)
                self.entry_durasi_berhenti.insert(0, "nilai tdk bnr!")
        else :
            try :
                self.durasi_berhenti = int(self.entry_durasi_berhenti.get()) * 60
            except :
                self.entry_durasi_berhenti.delete(0, END)
                self.entry_durasi_berhenti.insert(0, "nilai tdk bnr!")
            else :
                self.sisa_waktu = self.durasi_pomodoro
                menit = self.sisa_waktu // 60
                detik = self.sisa_waktu % 60
                self.label_sisa_waktu.config(text= f"{menit:02d}:{detik:02d}")


window = Tk()
window.title("Pomodoro Timer")
window.maxsize(width= 425, height= 275)
window.minsize(width= 425, height= 275)
window.config(bg = "#1A1A2E")
pomodoro = Pomodoro(window)
pomodoro.pack(expand= True)
window.mainloop()
pomodoro.keluar = True
