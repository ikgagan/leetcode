# Question: Binary Search
# Description:
# Given a sorted array of integers nums and a target value, return the index of the target if it exists. If not, return -1.

# Example:
# Input: nums = [-1,0,3,5,9,12], target = 9
# Output: 4
# Explanation: The target 9 is at index 4.

def binary_search(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1

    while left <= right:
        # Calculate the middle index
        mid = (left + right) // 2

        # Check if target is found
        if nums[mid] == target:
            return mid
        # If target is smaller, ignore the right half
        elif nums[mid] > target:
            right = mid - 1
        # If target is larger, ignore the left half
        else:
            left = mid + 1

    # Target not found
    return -1


nums = [-1, 0, 3, 5, 9, 12]

target = 9
print(binary_search(nums, target))  # Output: 4

target = 2
print(binary_search(nums, target))  # Output: -1
