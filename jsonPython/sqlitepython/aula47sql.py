# ESCREVENDO DENTRO DE SQLITE

from os import error
import sqlite3
from sqlite3 import Error

#"C:\bancos\bancopython\agenda.db"




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



####################  criar tabela

vsql="""CREATE TABLE tb_contatos(
        N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
        T_NOMECONTATO VARCHAR(30),
        T_TELEFONECONTATO VARCHAR(14),
        T_EMAILCONTATO VARCHAR(30)
    );"""


######## chamar event

def criarTabela(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Tabela criada com sucesso")

    except Error as ex:
        print(ex)



############### Chamada para criacao da tabela
criarTabela(vcon, vsql)


#------ fecha banco -----
vcon.close()