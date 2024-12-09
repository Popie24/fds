def insertion_sort(arr):
    """Sorts an array using insertion sort algorithm."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def shell_sort(arr):
    """Sorts an array using shell sort algorithm."""
    n = len(arr)
    gap = n // 2  # Start with a big gap, then reduce the gap
    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            # Shift earlier gap-sorted elements up until the correct location for arr[i] is found
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2

def display_top_five_scores(arr):
    """Displays the top five scores from the sorted array."""
    print("Top five scores:")
    for score in arr[-5:]:
        print(score)

# Sample data: percentages of students
percentages = [85.5, 92.0, 78.5, 88.0, 95.5, 67.0, 82.5, 90.0, 76.5, 89.0]

# Insertion Sort
insertion_sorted_percentages = percentages.copy()
insertion_sort(insertion_sorted_percentages)
print("Sorted percentages using Insertion Sort:")
print(insertion_sorted_percentages)
display_top_five_scores(insertion_sorted_percentages)

# Shell Sort
shell_sorted_percentages = percentages.copy()
shell_sort(shell_sorted_percentages)
print("\nSorted percentages using Shell Sort:")
print(shell_sorted_percentages)
display_top_five_scores(shell_sorted_percentages)
