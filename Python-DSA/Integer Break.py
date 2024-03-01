def integer_break(n):
    if n == 2:
        return 1
    if n == 3:
        return 2
    if n == 4:
        return 4

    dp = [0] * (n + 1)
    dp[1] = 1
    dp[2] = 2
    dp[3] = 3
    dp[4] = 4
    for i in range(5, n + 1):
        max_product = 0
        for j in range(1, i + 1):
            max_product = max(max_product, dp[j] * dp[i - j])
            dp[i] = max_product
    return dp[n]


def main():
    n = int(input("Enter a positive integer: "))
    if n <= 0:
        print("Please enter a positive integer.")
    else:
        result = integer_break(n)
        print("The maximum product of breaking", n, "into positive integers is:", result)


if __name__ == "__main__":
    main()