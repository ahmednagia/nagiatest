import random

def insertion_sort(arr):
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be compared and placed in the correct position
        j = i - 1
        
        # Move elements of arr[0..i-1] that are greater than key to one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  # Shift element to the right
            j -= 1
        
        # Place key after the correct position
        arr[j + 1] = key
    
    return arr

def main():
    # Create a random list of numbers
    arr = random.sample(range(1, 101), 10)  # Random list of 10 numbers between 1 and 100
    print("Original List:", arr)
    
    # Apply insertion sort
    sorted_arr = insertion_sort(arr)
    
    # Print the sorted list
    print("Sorted List:", sorted_arr)

# Run the main function
main()
