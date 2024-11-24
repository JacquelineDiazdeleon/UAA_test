from __future__ import absolute_import

class App:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def resta(a, b):
        return a - b

    @staticmethod
    def multiplicacion(a, b):
        return a * b

    @staticmethod
    def division(a, b):
        if b == 0:
            return "Error: División por cero"
        return a / b

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

    @staticmethod
    def contar_pares(inicio, fin):
        return len([x for x in range(inicio, fin + 1) if x % 2 == 0])

    @staticmethod
    def maximo_multiplo(lista, num):
        multiplos = [x for x in lista if x % num == 0]
        return max(multiplos) if multiplos else None

    @staticmethod
    def es_palindromo(cadena):
        return cadena == cadena[::-1]

    @staticmethod
    def suma_primeros_impares(n):
        return sum([x for x in range(1, 2 * n, 2)])

    @staticmethod
    def elementos_unicos(lista):
        return len(lista) == len(set(lista))

    @staticmethod
    def calcular_factorial(n):
        if n == 0 or n == 1:
            return 1
        factorial = 1
        for i in range(2, n + 1):
            factorial *= i
        return factorial

    @staticmethod
    def contar_vocales(cadena):
        return sum(1 for char in cadena.lower() if char in 'aeiou')

    @staticmethod
    def segundo_mayor(lista):
        if len(lista) < 2:
            return None
        lista_unica = list(set(lista))
        lista_unica.sort(reverse=True)
        return lista_unica[1] if len(lista_unica) > 1 else None

    @staticmethod
    def fibonacci(n):
        if n == 0:
            return []
        if n == 1:
            return [0]
        seq = [0, 1]
        for i in range(2, n):
            seq.append(seq[-1] + seq[-2])
        return seq
