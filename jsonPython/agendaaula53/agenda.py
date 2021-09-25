import os
import sqlite3
from sqlite3 import Error



# ----  conexao com o banco



######### Criar conexao
def ConexaoBanco():
    caminho = "C:\\bancos\\bancopython\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    
    except Error as ex:
        print(ex)
    return con


vcon = ConexaoBanco()

# ---------------- end conexao com banco ---------------------------



# --------------- menu principal --------------------------------

def menuPrincipal():
    os.system("cls")
    print("1 - Inserir novo registro no bd")
    print("2 - Deletar registro no BD")
    print("3 - Atualizar registro no BD")
    print("4 - Consultar registro por ID")
    print("5 - Consultar registro por nome no BD")
    print("6 - Sair")


def  menuInserir():
    pass

def menuDeletar():
    pass

def menuAtulizar():
    pass

def menuConsultarID():
    pass

def menuConsultarNome():
    pass

def menuSair():
    os.system("cls")
    print("Programa foi finalizado")

opcao = 0
try:
    while opcao != 6:
        try:
            menuPrincipal()
            opcao = int(input("Digite uma opcao: "))
        except ValueError as ex:
            print(ex)
            
        try:
            int(opcao)  
            if opcao == 1:
                menuInserir()
                
            elif opcao == 2:
                menuDeletar()
                
            elif opcao == 3:
                menuAtulizar()
            
            elif opcao == 4:
                menuConsultarID()
            
            elif opcao == 5:
                menuConsultarNome()
        
            elif opcao == 6:
                menuSair()
                
            else:
                os.system("cls")
                print("opcao usada invalida")
                os.system("pause")

        except ValueError:
            os.system("cls")
          

except SyntaxError as ex:
    print(ex)
    pass

os.system("pause")







