# Regex
import re 

texto = "Curso de Python do CFB curso, canal youtube"

res = re.findall("python", texto, re.IGNORECASE)
print(res)




