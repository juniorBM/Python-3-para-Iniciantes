#String é imutavel não pode ser mudado o valor pelo index
nome = "junior"

#Acessando caracter pelo index
print(nome[0])

#Para alterar, só converter para uma lista
lista = list(nome)
print(lista)
lista[0] = "t"
print(lista)
nome = ''.join(lista)
print(nome)