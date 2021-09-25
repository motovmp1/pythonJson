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



#---------------------  delete itens  -----------------------------

vsql = """DELETE FROM tb_contatos 
                            WHERE N_IDCONTATO=4
                            

"""
cvsql = """
        
        SELECT * FROM tb_contatos
"""
#SELECT COUNT(*) FROM tb_contatos WHERE N_IDCONTATO=4
#---------------------  end delete itens -----------------------------




#---------  deletar dados bd criado ----------

def deletar(conexao, sql, cvsql):
    try:
        c=conexao.cursor()
        c.execute(sql)
        print("Registros removido com sucesso")
        conexao.commit()
        print("commit success....")
        c.execute(cvsql)
        resultado = c.fetchall()
        for r in resultado:
            print(r)
        
    except Error as ex:
        print(ex)
    
    finally:
        print("rotina deletar finalizada com success....")



# -------   end conexao do banco de dados ----------



deletar(vcon, vsql, cvsql)
