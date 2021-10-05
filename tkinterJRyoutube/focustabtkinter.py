from tkinter import *



# --------------------------------------------------------------
# GUI
menu_inicial = Tk()
menu_inicial.title("FCT 1 - v.0.0.1")

# ----------------------------------------------------------------
# Funcoes


# ----------------------------------------------------------------
# widgets

# geometry - posso usar largura altura e local
menu_inicial.geometry("900x500+200+200")

# resize da janela
menu_inicial.resizable(True, True)

# tamanho minimo e maximo da janela
menu_inicial.minsize(width=500, height=500)
menu_inicial.maxsize(1250,900)

t1  = Entry(menu_inicial)
t2  = Entry(menu_inicial)
t3  = Entry(menu_inicial)

# ------------------------------------------------------------------
# layouts

t1.grid()
t2.grid()
t3.grid()


# Focus
t1.focus()




# -----------------------------------------------------------------------
# loop principal
menu_inicial.mainloop()