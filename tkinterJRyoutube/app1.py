from tkinter import *

menu_inicial = Tk()
menu_inicial.title("FCT 1 - v.0.0.1")

# geometry - posso usar largura altura e local
menu_inicial.geometry("900x500+200+200")

# resize da janela
menu_inicial.resizable(True, True)

# tamanho minimo e maximo da janela
menu_inicial.minsize(width=500, height=500)
menu_inicial.maxsize(1250,900)


menu_inicial.mainloop()

