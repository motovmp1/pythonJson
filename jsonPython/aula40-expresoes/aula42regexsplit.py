import re # Expressoes regulares

texto = "Curso de Python do FCB cursos, canal youtube"

res = re.split(" ", texto)

print(res)
print(res[2])

for t in res:
    print(t)

