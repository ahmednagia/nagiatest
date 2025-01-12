def factorial(n):
    # Base case: if n is 1 or 0, return 1 (since 1! = 1 and 0! = 1)
    if n == 0 or n == 1:
        return 1
    # Recursive case: n! = n * (n-1)!
    else:
        return n * factorial(n - 1)

# Example usage
def main():
    number = 5  # Example number for which we want to calculate the factorial
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")

main()
