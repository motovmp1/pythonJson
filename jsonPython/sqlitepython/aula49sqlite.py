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


#---------------------  end conexao -----------------------------

vsql = """INSERT INTO tb_contatos 
                        (T_NOMECONTATO, T_TELEFONECONTATO, T_EMAILCONTATO) 
                        VALUES('teste_nome', 'teste_telefone', 'teste_email')

"""


#---------  inserir dados bd criado ----------

def inserir(conexao, sql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Registros inseridos com sucesso")
        conexao.commit()
        print("commit success....")
        
    except Error as ex:
        print(ex)

# -------   end conexao do banco de dados ----------



inserir(vcon, vsql)
