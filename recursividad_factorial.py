def main():
    def factorial(n):
        """Calcula el factorial de n.

        n int > 0
        returns n!
        """
        if n == 1 or 0:
            return 1
        else:
            return n * factorial(n-1)

    n = int(input('Digite un número: '))
    print(f'El factorial de {n} es {factorial(n)}')
        
if __name__ == '__main__':
    main()