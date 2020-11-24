# Función de búsqueda binaria

#!/usr/bin/env python
# encoding: latin1

size = 25
primes = ([2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])

def binarySearch(x):
    x = x
    min = 0
    max = size - 1
    while (min <= max):
        guess = min + (max - min) // 2
        if primes[guess] == x:
            return guess
        elif primes[guess] < x:
            min = guess + 1
        else:
            max = guess - 1
    return ("Valor no encontrado")
 
if __name__ == "__main__":
    x = int(input("Escriba un número: "))
    position = binarySearch(x)
    print(position)