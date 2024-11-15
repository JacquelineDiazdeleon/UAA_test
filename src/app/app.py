from __future__ import absolute_import

class App:
    @staticmethod
    def add(a,b):
        return a+b

    def resta(a,b):
        return 0

    def multiplicacion(a,b):
        return 0

    def division(a,b):
        return 0

    # 1. Verifica si una lista contiene un número primo
def contiene_numero_primo(lista):
    """
    Verifica si hay al menos un número primo en la lista.
    Retorna True si hay un número primo, de lo contrario, False.
    """
    def es_primo(num):
        if num < 2:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True
    
    return any(es_primo(num) for num in lista)


pass

    # 2. Cuenta los números pares en un rango dado
"""
    Cuenta la cantidad de números pares en el rango desde 'inicio' hasta 'fin' (inclusive).
    Retorna la cantidad de números pares.
"""
def contar_pares(inicio, fin):
    return sum(1 for num in range(inicio, fin + 1) if num % 2 == 0)

pass

    # 3. Encuentra el número máximo en una lista que sea múltiplo de un valor dado
def maximo_multiplo(lista, multiplo):
    multiplos = [num for num in lista if num % multiplo == 0]
    return max(multiplos) if multiplos else None

"""
    Encuentra y retorna el valor máximo de la lista que es múltiplo del parámetro 'multiplo'.
    Si no hay múltiplos, retorna None.
"""

pass

    # 4. Verifica si una palabra es palíndroma (se lee igual en ambos sentidos)
def es_palindromo(palabra):
    return palabra == palabra[::-1]
"""
        Verifica si la palabra es un palíndromo (igual al leerla al revés).
        Retorna True si es palíndromo, de lo contrario, False.
        """
pass

    # 5. Calcula la suma de los primeros n números impares
def suma_primeros_impares(n):
    return sum(2 * i + 1 for i in range(n))
"""
        Calcula y retorna la suma de los primeros 'n' números impares.
        """
pass

    # 6. Verifica si todos los elementos de una lista son únicos
def elementos_unicos(lista):
    return len(lista) == len(set(lista))
"""
        Verifica si todos los elementos de la lista son únicos.
        Retorna True si son únicos, de lo contrario, False.
        """
pass

    # 7. Calcula el factorial de un número sin usar recursión
def calcular_factorial(numero):
    factorial = 1
    for i in range(2, numero + 1):
        factorial *= i
    return factorial

"""
        Calcula y retorna el factorial de 'numero' usando un ciclo.
        """
pass

    # 8. Cuenta la cantidad de vocales en una cadena
def contar_vocales(cadena):
    return sum(1 for char in cadena.lower() if char in "aeiou")

"""
        Cuenta y retorna la cantidad de vocales en la cadena.
        """
pass

    # 9. Encuentra el segundo número mayor en una lista
def segundo_mayor(lista):
    if len(lista) < 2:
        return None
    lista = list(set(lista))
    lista.sort(reverse=True)
    return lista[1] if len(lista) > 1 else None

"""
        Encuentra y retorna el segundo número más grande en la lista.
        Si no existe, retorna None.
        """
pass

    # 10. Calcula la serie de Fibonacci hasta n términos
def fibonacci(n):
    if n == 0:
        return []
    fib_sequence = [0, 1]
    for i in range(2, n):
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])
    return fib_sequence[:n]

"""
        Genera y retorna una lista con los primeros 'n' términos de la serie de Fibonacci.
        """
pass
