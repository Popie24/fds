def quick_sort(arr):
    """Sorts an array using the quick sort algorithm."""
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]  # Choose the middle element as the pivot
        left = [x for x in arr if x < pivot]  # Elements less than pivot
        middle = [x for x in arr if x == pivot]  # Elements equal to pivot
        right = [x for x in arr if x > pivot]  # Elements greater than pivot
        return quick_sort(left) + middle + quick_sort(right)

def display_top_five_scores(arr):
    """Displays the top five scores from the sorted array."""
    print("Top five scores:")
    # Ensure that no error occurs if there are fewer than 5 scores
    for score in arr[-5:]:
        print(score)

# Sample data: percentages of students
percentages = [85.5, 92.0, 78.5, 88.0, 95.5, 67.0, 82.5, 90.0, 76.5, 89.0]

# Quick Sort
sorted_percentages = quick_sort(percentages)
print("Sorted percentages using Quick Sort:")
print(sorted_percentages)

# Display the top five scores
display_top_five_scores(sorted_percentages)
