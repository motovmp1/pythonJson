import re # Expressoes regulares

texto = "Curso de Python do FCB cursos, canal youtube"

res = re.sub(",", "." ,texto)

print(res)

