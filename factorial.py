#factorial
def factorial(n):
    return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

n = int(input("Enter a number: "))
print(factorial(n))


