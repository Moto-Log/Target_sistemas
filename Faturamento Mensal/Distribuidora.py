import json

with open("dados.json",encoding='utf-8') as dados_fat:
    fat = json.load(dados_fat)

menor = 999999
maior = 0
media = 0
cont = 0
num_sup = 0
dias_sup = []

for i in fat:
    if i['valor'] == 0:
        continue
    if menor > i['valor']:
        menor = i['valor']
        menord = i['dia']
    if maior < i['valor']:
        maior = i['valor']
        maiord = i['dia']
    media += i['valor']
    cont +=1
media = media/cont
for i in fat:
    if i['valor'] > media:
        num_sup = num_sup + 1

print("O menor valor faturado foi: R$ %.4f no dia %s"%(menor,menord))
print("O maior valor faturado foi: R$ %.4f no dia %s"%(maior,maiord))
print("A media mensal de faturamento foi: R$ %.4f"%(media))
print("Houveram %d dias que o faturamento superou a media mensal"%(num_sup))