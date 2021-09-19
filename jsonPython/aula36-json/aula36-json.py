import json

# cuidado, json format estiver errado o python retorna erro e nao eh facil verificar 
carros_json = '{"marca": "honda", "modelo": "HRV", "cor": "prata"}'


carros = json.loads(carros_json)



