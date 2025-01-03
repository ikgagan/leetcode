# Question: Intersection of Two Arrays
# Problem:
# Given two integer arrays nums1 and nums2, return an array of their intersection.
# Each element in the result must appear as many times as it shows in both arrays.

# Example:
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]

def intersect(nums1: list[int], nums2: list[int]) -> list[int]:
    # Dictionary to store the frequency of elements in nums1
    counts = {}
    for num in nums1:
        counts[num] = counts.get(num, 0) + 1

    result = []
    # Traverse nums2 to find common elements
    for num in nums2:
        if counts.get(num, 0) > 0:
            result.append(num)
            counts[num] -= 1

    return result

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
print(intersect(nums1, nums2))  # Output: [2, 2]

nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]
print(intersect(nums1, nums2))  # Output: [9, 4]
