import random

# Function to merge two sorted halves
def merge(left, right):
    sorted_array = []
    i = j = 0

    # Merge the two halves while comparing their elements
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            sorted_array.append(left[i])
            i += 1
        else:
            sorted_array.append(right[j])
            j += 1

    # If there are any remaining elements in left, append them
    while i < len(left):
        sorted_array.append(left[i])
        i += 1

    # If there are any remaining elements in right, append them
    while j < len(right):
        sorted_array.append(right[j])
        j += 1

    return sorted_array

# Function to perform merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr  # Base case: array is already sorted if it has one element

    # Divide the array into two halves
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    # Recursively sort both halves and merge them
    return merge(merge_sort(left), merge_sort(right))

# Main function to generate a random array and sort it
def main():
    # Generate a random list of numbers
    arr = random.sample(range(1, 101), 10)  # Random list of 10 numbers between 1 and 100
    print(f"Original array: {arr}")

    # Sort the array using merge sort
    sorted_arr = merge_sort(arr)

    # Print the sorted array
    print(f"Sorted array: {sorted_arr}")

# Call the main function
main()
