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


Label(menu_inicial, width=20, bg="red").grid()
Label(menu_inicial, width=20, bg="green").grid(column=1)
# posso escolher os dois lados para que nao haja gaps entre labels
Label(menu_inicial, width=40, bg="blue").grid(column=0, columnspan=2, sticky='we')



menu_inicial.mainloop()