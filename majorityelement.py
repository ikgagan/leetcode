# Question :  Majority Element
# Problem:
# Given an array nums of size 
# 𝑛
# n, return the majority element.
# The majority element is the element that appears more than 
# ⌊
# 𝑛
# /
# 2
# ⌋
# ⌊n/2⌋ times.
# Assume the array is non-empty and a majority element always exists.

# Example:
# Input: nums = [3,2,3]
# Output: 3

def majorityElement(nums: list[int]) -> int:
  # Boyer-Moore Algorithm
    candidate = None
    count = 0

    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif num == candidate:
            count += 1
        else:
            count -= 1

    return candidate


nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
