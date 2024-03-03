def search_in_sorted_matrix(matrix, target):
    if not matrix or not matrix[0]:
        return False
    
    rows = len(matrix)
    cols = len(matrix[0])
    
    # Start from the top-right corner
    row = 0
    col = cols - 1
    
    while row < rows and col >= 0:
        if matrix[row][col] == target:
            return True
        elif matrix[row][col] < target:
            # Move downwards if current element is less than target
            row += 1
        else:
            # Move leftwards if current element is greater than target
            col -= 1
    
    return False

# Example usage:
matrix = [
    [1, 4, 7, 11],
    [2, 5, 8, 12],
    [3, 6, 9, 16],
    [10, 13, 14, 17]
]

target = 6
print(search_in_sorted_matrix(matrix, target))  # Output: True
