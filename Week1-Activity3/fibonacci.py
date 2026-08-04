
def print_fibonacci(n):
    a, b = 0, 1
    print("Fibonacci series up to", n, ":")
    while a <= n:
        print(a, end=" ")
        a, b = b, a + b
    print()


def calculate_factorial(n):
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    return factorial


def main():
    n = int(input("Enter a number (N): "))

    print_fibonacci(n)

    fact = calculate_factorial(n)
    print("Factorial of", n, "is:", fact)


main()