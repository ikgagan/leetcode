# Question: Remove Duplicates from Sorted Array
# Description:
# Given an integer array nums sorted in non-decreasing order, remove duplicates in-place so that each unique element appears only once. Return k as the number of unique elements.

# Example:
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]


def remove_duplicates(nums: list[int]) -> int:
    if not nums:  # Edge case for an empty array
        return 0

    # Initialize the slow pointer
    slow = 0

    # Traverse the array with the fast pointer
    for fast in range(1, len(nums)):
        if nums[fast] != nums[slow]:  # New unique element found
            slow += 1
            nums[slow] = nums[fast]

    # Return the count of unique elements (1-based index)
    return slow + 1

nums = [1, 1, 2]
k = remove_duplicates(nums)
print(f"Number of unique elements: {k}")  # Output: 2
print(f"Modified array: {nums[:k]}")      # Output: [1, 2]
