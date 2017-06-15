#Quando uma função chama ela mesmo
'''
fat(3) = 3 * fat(2) = 3 * 2 = 6
fat(2) = 2 * fat(1) = 2 * 1 = 2
fat(1) = 1 * fat(0) = 1 * 1 = 1
fat(0) = 1
'''
def fat(n):
    if n == 0:
        return 1
    return n * fat(n - 1)

print(fat(5))