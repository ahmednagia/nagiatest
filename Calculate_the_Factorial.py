def main():
    # Step 1: Take user input for the number
    num = int(input("Enter a number to calculate its factorial: "))

    # Step 2: Initialize a variable to store the factorial result
    factorial = 1

    # Step 3: Loop to calculate the factorial
    for i in range(1, num + 1):
        factorial *= i  # Multiply factorial by the current number

    # Step 4: Print the result
    print(f"The factorial of {num} is {factorial}")

# Call the main function
main()
