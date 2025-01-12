def fibonacci(n):
    # Base case: if n is 0 or 1, return n (F(0) = 0, F(1) = 1)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
def main():
    number = 6  # Example number for which we want to calculate the Fibonacci sequence
    result = fibonacci(number)
    print(f"The Fibonacci number at position {number} is: {result}")

main()
