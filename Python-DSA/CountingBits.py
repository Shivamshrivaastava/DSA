def count_bits(n):
    # Initialize a list to store the count of set bits for each number from 0 to n
    result = [0] * (n + 1)

    for i in range(1, n + 1):
        # Count the set bits in i by repeatedly dividing by 2 and counting remainder
        count = 0
        while i:
            count += i & 1
            i >>= 1
        result[i] = count

    return result

# Example usage:
n = 5
print(count_bits(n))  # Output: [0, 1, 1, 2, 1, 2]
