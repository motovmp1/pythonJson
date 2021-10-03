from tkinter import *


menu_inicial = Tk()
menu_inicial.title("FCT 1 - v.0.0.1")

# geometry - posso usar largura altura e local
menu_inicial.geometry("900x500+200+200")


label_1 = Label(menu_inicial, 
                            text="Teste de label 1",
                            bg="yellow",
                            fg="gray",
                            font="Arial 12")
label_1.pack()


label_2 = Label(menu_inicial, 
                            text="Teste de label 2",
                            font="Arial 12")
label_2.pack()




menu_inicial.mainloop()