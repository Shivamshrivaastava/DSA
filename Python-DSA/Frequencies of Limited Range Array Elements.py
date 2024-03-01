def frequency_of_elements(arr, n, limit):
    freq = [0] * limit

    # Counting frequencies of elements
    for i in range(n):
        freq[arr[i]] += 1

    # Printing frequencies
    for i in range(1, limit):
        print("Frequency of", i, ":", freq[i])

# Test the function
if __name__ == "__main__":
    # Sample array and sum
    arr = [1, 3, 2, 3, 4, 1, 6, 4, 3]
    n = len(arr)
    limit = max(arr) + 1

    # Call the function
    frequency_of_elements(arr, n, limit)
