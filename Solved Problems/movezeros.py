# Question: Move Zeroes
# Problem:
# Given an integer array nums, move all 0s to the end while maintaining the relative order of the non-zero elements.
# You must do this in-place without making a copy of the array.

# Example:
# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]


def moveZeroes(nums: list[int]) -> None:
    
    last_non_zero = 0  # Pointer for the position of the next non-zero element

    # Move all non-zero elements to the front
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero] = nums[i]
            last_non_zero += 1

    # Fill the remaining positions with zeros
    for i in range(last_non_zero, len(nums)):
        nums[i] = 0

# Test cases
nums = [0, 1, 0, 3, 12]
moveZeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]

nums = [0, 0, 0]
moveZeroes(nums)
print(nums)  # Output: [0, 0, 0]

nums = [1, 2, 3]
moveZeroes(nums)
print(nums)  # Output: [1, 2, 3]
