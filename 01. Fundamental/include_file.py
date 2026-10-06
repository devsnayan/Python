def bubble_sort(penguins):
    n = len(penguins)

    # Outer loop for each penguin in the parade
    for i in range(n):
        # Inner loop for the penguin comparisons and swaps
        for j in range(0, n-i-1):
            # Compare adjacent penguins
            if penguins[j] > penguins[j+1]:
                # Swap places if the penguin is taller
                penguins[j], penguins[j+1] = penguins[j+1], penguins[j]

# Example usage:
penguins_heights = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]

print("Unsorted Penguin Parade:", penguins_heights)

# Let's sort the penguins using Bubble Sort
bubble_sort(penguins_heights)

print("Sorted Penguin Parade:", penguins_heights)
