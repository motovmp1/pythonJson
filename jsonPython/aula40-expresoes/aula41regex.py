import re # Expressoes regulares

texto = "Curso de Python do FCB cursos, canal youtube"

res = re.search("Curso", texto)

print(res.span())
print(res.start())
print(res.end())
