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
@staticmethod
def contiene_numero_primo(lista):
        def es_primo(n):
            if n < 2:
                return False
            for i in range(2, int(n**0.5) + 1):
                if n % i == 0:
                    return False
            return True

        return any(es_primo(num) for num in lista)

    # Método para contar números pares en un rango
@staticmethod
def contar_pares(inicio, fin):
        return len([x for x in range(inicio, fin + 1) if x % 2 == 0])

    # Método para encontrar el máximo múltiplo de un número en una lista
@staticmethod
def maximo_multiplo(lista, num):
        multiplos = [x for x in lista if x % num == 0]
        return max(multiplos) if multiplos else None

    # Método para verificar si una cadena es un palíndromo
@staticmethod
def es_palindromo(cadena):
        return cadena == cadena[::-1]

    # Método para sumar los primeros n números impares
@staticmethod
def suma_primeros_impares(n):
        return sum([x for x in range(1, 2 * n, 2)])

    # Método para verificar si todos los elementos de una lista son únicos
@staticmethod
def elementos_unicos(lista):
        return len(lista) == len(set(lista))

    # Método para calcular el factorial de un número
@staticmethod
def calcular_factorial(n):
        if n == 0 or n == 1:
            return 1
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

    # Método para contar vocales en una cadena
@staticmethod
def contar_vocales(cadena):
        return sum(1 for char in cadena.lower() if char in 'aeiou')

    # Método para encontrar el segundo número mayor en una lista
@staticmethod
def segundo_mayor(lista):
        if len(lista) < 2:
            return None
        lista_unica = list(set(lista))
        lista_unica.sort(reverse=True)
        return lista_unica[1] if len(lista_unica) > 1 else None

    # Método para generar una secuencia de Fibonacci
@staticmethod
def fibonacci(n):
        if n == 0:
            return []
        if n == 1:
            return [0]
        secuencia = [0, 1]
        for i in range(2, n):
            secuencia.append(secuencia[-1] + secuencia[-2])
        return secuencia