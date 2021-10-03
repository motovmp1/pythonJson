from tkinter import *


menu_inicial = Tk()
menu_inicial.title("FCT 1 - v.0.0.1")

# geometry - posso usar largura altura e local
menu_inicial.geometry("900x500+200+200")


label_1 = Label(menu_inicial, 
                            text="Teste de label 1",
                            bg="#d9d9d9",
                            fg="#333333",
                            font="Arial 12",
                            width=20,
                            bd=1,
                            relief="solid",
                            highlightbackground="#37d3ff")
label_1.pack()


label_2 = Label(menu_inicial, 
                            text="Teste de label 2",
                            font="Arial 12")
label_2.pack()




menu_inicial.mainloop()