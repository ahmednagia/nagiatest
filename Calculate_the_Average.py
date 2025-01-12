def calculate_average(numbers):
    # Get the sum of the list using sum() function
    total = sum(numbers)
    
    # Divide the sum by the length of the list to get the average
    average = total / len(numbers) if len(numbers) > 0 else 0  # To handle an empty list
    
    return average

# Example usage
def main():
    nums = [10, 20, 30, 40, 50]  # Example list of numbers
    result = calculate_average(nums)
    print(f"The average of the list is: {result}")

main()
