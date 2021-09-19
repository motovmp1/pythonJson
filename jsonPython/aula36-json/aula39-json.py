import json


def linha():
    print("============ space ======================")
    print(" ")

#pode usar r se quiser
with open('./aula36-json/jogador.json') as f:
    jogador = json.load(f)

for c in jogador:
    print(c)

linha()

#itens
for i in jogador.items():
    print(i)

linha()

#valores
for v in jogador.values():
    print(v)

linha()

