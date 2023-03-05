import json

with open("dist.json",encoding='utf-8') as dados_dist:
    dados = json.load(dados_dist)

soma = 0

for i in dados:
    soma += i['valor']
for i in dados:
    print("Participação de %s: %.2f%%"%(i['UF'],(i['valor']/soma)*100))
print("Total: R$ %.2f"%(soma))