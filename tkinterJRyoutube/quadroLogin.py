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


Label(menu_inicial, text="Usuario: ").grid(row=0, column=0, sticky=W)
Label(menu_inicial, text="Senha: ").grid(row=1, column=0, sticky=W)

texBox_usuario = Entry(menu_inicial).grid(row=0, column=1)
texBox_senha = Entry(menu_inicial).grid(row=1, column=1)


cmd_login = Button(menu_inicial, text="Login").grid(row=2, column=1, sticky=E)

menu_inicial.mainloop()