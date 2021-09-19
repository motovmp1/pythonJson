# Regex
import re 

texto = "Curso de Python do CFB curso, canal youtube"

pesq = input("Pesquisar: ")

res = re.findall(pesq, texto, re.IGNORECASE)
print(res)

qtde = len(res)

print("Qtde: " + str(qtde))

for t in res:
    print(t)

