def factorial(n):
    """Calculate n's factorial

    n int > 0
    return n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n - 1)

n = int(input('Write an integer: '))

print(factorial(n))
