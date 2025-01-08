import random

def bubble_sort(arr):
    n = len(arr)
    # Traverse through all elements in the list
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap the elements
    return arr

def main():
    # Create a random list of numbers
    arr = random.sample(range(1, 101), 10)  # Random 10 numbers between 1 and 100
    print("Original list:", arr)
    
    # Sort the list using bubble sort
    sorted_arr = bubble_sort(arr)
    
    # Print the sorted list
    print("Sorted list:", sorted_arr)

# Call the main function
main()
