aparicoes={
    "guilherme":1,
    "ernesto":2,
    "nome":3,
    "vindo":2
}

print(f"o valor para a  chave é {aparicoes['guilherme']}")

#método para verificar se há alguma chave e retornar, se não houver, retorna algo
#nesse caso retorna 0
print(aparicoes.get("ernesto",0))

#operações
#adicionando:
aparicoes["carlos"]=["bolo,pizza"]
print(aparicoes)

#substituir valor:
aparicoes["ernesto"]=3
print(aparicoes)

#remover valor:
del(aparicoes["vindo"])
print(aparicoes)

#verificar se está dentro do dicionario,faz uma busca nas chaves
teste="ernesto" in aparicoes
print(teste)

#iterar pelos elementos:
#printa as chaves
for elemento in aparicoes:
    print(elemento)
    
    
#iterando pelos values
for values in aparicoes.values():
    print(values)
    
    
#valor e chave

for elemento in aparicoes:
    print(f"elemento: {elemento} chave: {aparicoes[elemento]}")
    
    
#passando pela dupla
for elemento in aparicoes.items():
    print(elemento)
    
    
#desempacotando
for chave,valor in aparicoes.items():
    print(chave, "=", valor)
    
    
    
meu_texto="Bem vindo, meu nome é Ernesto eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
meu_texto=meu_texto.lower()
aparicoes={}

#contando a quantidade de aparições da palavra no texto
for palavra in meu_texto.split():
    ate_agora=aparicoes.get(palavra,0)
    aparicoes[palavra]=ate_agora+1
    
    
print(aparicoes)
    