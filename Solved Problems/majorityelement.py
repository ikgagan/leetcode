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


def majorityElement(nums: list[int]) -> int:
    # Using a Hash Map (Frequency Count)
    # Dictionary to count occurrences of each element
    counts = {}
    n = len(nums)

    for num in nums:
        counts[num] = counts.get(num, 0) + 1
        # Check if the current element is the majority
        if counts[num] > n // 2:
            return num

    # In case we don't return early (guaranteed majority exists)
    for num, count in counts.items():
        if count > n // 2:
            return num

nums = [3, 2, 3]
print(majorityElement(nums))  # Output: 3

nums = [2, 2, 1, 1, 1, 2, 2]
print(majorityElement(nums))  # Output: 2
