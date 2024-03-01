def majority_element(nums):
    if not nums:
        return []

    candidate1, count1 = None, 0
    candidate2, count2 = None, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1 = num
            count1 = 1
        elif count2 == 0:
            candidate2 = num
            count2 = 1
        else:
            count1 -= 1
            count2 -= 1

    count1 = count2 = 0
    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1

    majority_elements = []
    if count1 > len(nums) // 3:
        majority_elements.append(candidate1)
    if count2 > len(nums) // 3:
        majority_elements.append(candidate2)

    return majority_elements

def main():
    nums = [3, 2, 3]
    print("Input:", nums)
    print("Majority Elements:", majority_element(nums))

    nums = [1, 1, 1, 3, 3, 2, 2, 2]
    print("\nInput:", nums)
    print("Majority Elements:", majority_element(nums))

if __name__ == "__main__":
    main()
