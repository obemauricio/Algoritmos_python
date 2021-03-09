def multiply_bytwo(n):
    return n * 2

def add_2(n):
    return n + 2

def apply_operation(f, numero):
    results = []
    for i in numero:
        result = f(numero)
        results.append(result)

nums = [1, 2, 3]

apply_operation(multiply_bytwo, nums)

print(apply_operation)