lista = [1, 2, 3]

#Removendo elemento da lista, passando o elemento para ser removido
lista.remove(1)
print(lista)

#Removendo elemento da lista, passando o index 
lista.pop(0)
print(lista)

#Limpar lista
lista2 = [1, 2, 3]
print("Lista2: ", lista2)
lista2.clear()
print("Lista limpada: ", lista2)

#Retornar indice de um elemento
lista3 = [1, 2, 3, 4]
print("Lista3: ", lista3)
print("Lista3 Index: ", lista3.index(2))

#Contar quantidade de elemento que aparece na lista
lista4 = ["junior", "junior", "python"]
print("Lista4: ", lista4)
print("Lista4, quantidade de vezes que aparece a palavra 'junior': ", lista4.count("junior"))

#Ordenar lista crescentemente
lista5 = [10, 7, 59, 0 , -1, 1]
print("Lista5: ", lista5)
lista5.sort()
print("Lista5, ordenada crescentemente: ", lista5)