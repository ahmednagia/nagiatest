import math

def main():
    # Step 1: Take input from the user
    N = int(input("Enter a number (N) to find all prime numbers between 2 and N: "))
    
    # Step 2: Loop through numbers from 2 to N
    for num in range(2, N+1):
        # Step 3: Check if the number is prime
        is_prime = True  # Assume the number is prime
        for i in range(2, int(math.sqrt(num)) + 1):  # Check divisibility up to the square root of num
            if num % i == 0:
                is_prime = False  # num is divisible by i, so it's not prime
                break
        
        # Step 4: Print the number if it's prime
        if is_prime:
            print(num)

# Call the main function
main()
