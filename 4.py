def selection_sort(arr):
    """Sorts an array using selection sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Assume the minimum is the first element of the unsorted part
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        # Swap the found minimum element with the first element of the unsorted part
        arr[i], arr[min_index] = arr[min_index], arr[i]

def bubble_sort(arr):
    """Sorts an array using bubble sort algorithm."""
    n = len(arr)
    for i in range(n):
        # Track if a swap was made
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap if the element found is greater than the next element
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        # If no two elements were swapped, the array is sorted
        if not swapped:
            break

def display_top_scores(arr, top_n=5):
    """Display the top N scores from the sorted array."""
    print(f"Top {top_n} scores:")
    for score in arr[-top_n:]:
        print(score)

if __name__ == "__main__":
    # Sample data: first year percentages of students
    percentages = [85.5, 92.0, 78.5, 88.0, 95.5, 67.0, 82.5, 90.0, 76.5, 89.0]

    # Sort using Selection Sort
    selection_sorted = percentages.copy()
    selection_sort(selection_sorted)
    print("Sorted percentages using Selection Sort:")
    print(selection_sorted)
    display_top_scores(selection_sorted)

    # Sort using Bubble Sort
    bubble_sorted = percentages.copy()
    bubble_sort(bubble_sorted)
    print("\nSorted percentages using Bubble Sort:")
    print(bubble_sorted)
    display_top_scores(bubble_sorted)
