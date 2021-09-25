import re # Regex Expressoes regulares

arquivo = open("../utils/teste.txt", "r")

#read = leitura
#a = append - anexar
#w = write escrita
#x cria arquivo





# aqui eu posso tratar como string e retorna usando comando regex
res = re.sub(" ", "-", arquivo.read())

arquivo.close()


print(res)

