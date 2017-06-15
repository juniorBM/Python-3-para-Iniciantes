from itertools import permutations
from itertools import combinations

lista = [1, 2, 3]

for p in permutations(lista):
    print(p)

for c in combinations(lista, 2):
    print(c)