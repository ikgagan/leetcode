#Question:  Power of Two
# Problem:
# Given an integer n, return true if it is a power of two. Otherwise, return false.
# Example:
# Input: n = 16
# Output: true
# Explanation: 2^4 =16


def isPowerOfTwo(n: int) -> bool:
    if n <= 0:
        return False
    while n % 2 == 0:
        n //= 2
    return n == 1

# Test cases
print(isPowerOfTwo(16))  # Output: True
print(isPowerOfTwo(18))  # Output: False
print(isPowerOfTwo(1))   # Output: True
print(isPowerOfTwo(0))   # Output: False
print(isPowerOfTwo(-2))  # Output: False
