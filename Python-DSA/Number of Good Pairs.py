# for any Given an array of integers nums, return the number of good pairs.

def num_good_pairs(nums):
    count = 0
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j]:
                count += 1
    return count

def main():
    nums = [int(x) for x in input("Enter space-separated integers: ").split()]
    print("Number of good pairs:", num_good_pairs(nums))

if __name__ == "__main__":
    main()
