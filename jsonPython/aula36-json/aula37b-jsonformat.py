import json
import typing_extensions


carros_dictionary={
    "marca": "honda",
    "modelo": "Hrv",
    "cor": "Prata"
}
#dictionary -> objeto em json


carros_list=["honda", "volkswagem", "ford", "fiat", "chevrolet"]
# list -> array json


carros_tuplas=("honda", "volkswagem", "ford", "fiat", "chevrolet")
# tupla -> array json


carros_j = json.dumps(carros_dictionary)
print(carros_j)


# aqui aceita elementos - depois virgula
carros_j = json.dumps(carros_dictionary, indent=4, separators=(":", "="), sort_keys=True)
print(carros_j)

