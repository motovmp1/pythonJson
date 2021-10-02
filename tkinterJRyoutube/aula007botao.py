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


# mudar fundo do formulario
# menu_inicial['bg'] = "blue"



# botao esta aqui
def cmd_Click(mensagem):
    print(mensagem)


# button evento  - precisa usar o lambda
btn = Button(menu_inicial, text="Executar", command=lambda: cmd_Click("Nova Mensagem"))
btn.pack()






menu_inicial.mainloop()