# Given an array arr of non-negative integers and an integer sum, the task is to count all subsets of the given array with a sum equal to a given sum.

def count_subsets_with_sum(arr, target_sum):
    n = len(arr)
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]

    # Base case initialization
    for i in range(n + 1):
        dp[i][0] = 1

    # Fill the dp table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            if arr[i - 1] <= j:
                dp[i][j] = dp[i - 1][j - arr[i - 1]] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]

    return dp[n][target_sum]

def main():
    arr = list(map(int, input("Enter the array of non-negative integers separated by space: ").split()))
    target_sum = int(input("Enter the target sum: "))
    result = count_subsets_with_sum(arr, target_sum)
    print("Count of subsets with sum equal to", target_sum, ":", result)

if __name__ == "__main__":
    main()
