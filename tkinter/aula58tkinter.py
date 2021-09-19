from tkinter import *
import os


c = os.path.dirname(__file__)
nomeArquivo=c+"\\nomes.txt"



def gravarDados():
    arquivo = open(nomeArquivo, "a")
    arquivo.write("Nome....: %s" % vnome.get())
    arquivo.write("\nTelefone: %s" % vfone.get())
    arquivo.write("\nObs.....: %s" % vobs.get("1.0", END))
    arquivo.write("\n\n")
    arquivo.close()
    print("Nome....: %s" % vnome.get())
    print("Telefone: %s" % vfone.get())
    print("Obs.....: %s" % vobs.get("1.0", END))



app =Tk()
app.title("CFB Cursos")
app.geometry("800x400")
app.configure(background="#dde")

# this is remove resize option
#app.resizable(0,0)


# anchor => N / S / E /W
# NE SE SO NO
Label(app, text="Nome", anchor=W).place(x=10, y=10, width=80, height=20,) 
vnome = Entry(app)
vnome.place(x=10, y=35, width=280, height=20)
vnome.focus_set()

Label(app, text="Telefone", anchor=W).place(x=10, y=70, width=80, height=20) 
vfone = Entry(app)
vfone.place(x=10, y=95, width=280, height=20)

Label(app, text="OBS", anchor=W).place(x=10, y=160, width=80, height=20) 
vobs = Text(app)
vobs.place(x=10, y=185, width=300, height=80)


btn = Button(app, text="Gravar Dados", command=gravarDados)
btn.place(x=10, y=290, width=150, height=30)


app.mainloop()