#Dicionario é a implementação de hash

#Dicionario é formado por um par chave e valor

d = {'marcos': 28, 'maria': 30}
print(d['maria'])

#Mostra as chaves do dicionario
print(d.keys())

#Deletar um chave do dicionario
del d['marcos']
print(d.keys())

#Retorna True ou False para saber se existe uma chave no dicionario
print('maria' in d)

#Mostra os valores do dicionario
print(d.values())