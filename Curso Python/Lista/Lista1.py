lista1 = [1, 2, 3, 4]
print(lista1)

lista2 = [1, 2, "Junior Mendonca"]
print(lista2)

print(lista2[2])

#Inserindo elementos na lista
lista3 = ["Comeco lista 3"]
lista3.append("Teste Inserção")
print(lista3)

#Acessando ultimo elemento
print(lista3[-1])

#Tamanho da lista
print(len(lista3))

#Extendendo a lista com uma outra lista
lista1.extend(lista3)
print(lista1)

#Inserindo em qualquer posição, primeiro paremetro posição e segundo elemento
lista1.insert(0, "Elemento inserido na posicao 0")
print(lista1)