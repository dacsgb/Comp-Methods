def factorial(n):
    f = 1
    if n > 0:
        f = n*factorial(n-1)
    return f

print(factorial(5))