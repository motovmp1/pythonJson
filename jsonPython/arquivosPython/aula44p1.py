
arquivo = open("../utils/teste.txt", "at")

#read = leitura
#a = append - anexar
#w = write escrita
#x cria arquivo


txt = input("Digite um texto aqui: ")
#arquivo.write("CFB Cursos")
arquivo.write(txt + "\n")



arquivo.close()
