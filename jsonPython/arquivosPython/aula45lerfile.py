import re # Regex Expressoes regulares

arquivo = open("../utils/teste.txt", "r")

#read = leitura
#a = append - anexar
#w = write escrita
#x cria arquivo




print(arquivo.read())

res = re.sub(" ", "-", arquivo.readline())



for leitura in arquivo:
    print(leitura)

arquivo.close()


print(res)