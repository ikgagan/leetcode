# Question : Palindrome Number
# Description:
# Given an integer x, return true if x is a palindrome, and false otherwise.

# An integer is a palindrome when it reads the same backward as forward. For example, 121 is a palindrome, but 123 is not.

# Example:
# Input: x = 121
# Output: true
# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore, it is not a palindrome.


def isPalindrome(x):
    # Handle negative numbers and numbers ending in 0 (except 0 itself)
    if x < 0 or (x % 10 == 0 and x != 0):
        return False
    
    reversed_half = 0
    # Reverse the second half of the number
    while x > reversed_half:
        reversed_half = reversed_half * 10 + x % 10
        x //= 10
    
    # Check if the number is a palindrome
    return x == reversed_half or x == reversed_half // 10

# Example Usage
print(isPalindrome(121))  # Output: True
print(isPalindrome(-121)) # Output: False
print(isPalindrome(10))   # Output: False
