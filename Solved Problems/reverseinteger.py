# Question: Reverse Integer
# Description:
# Given a signed 32-bit integer x, return x with its digits reversed.
# If reversing x causes the value to go outside the signed 32-bit integer range [-2^31, 2^31 - 1], return 0.

# Example:
# Input: x = 123
# Output: 321
# Input: x = -123
# Output: -321

def reverse(x):
    # Define the 32-bit integer range
    INT_MIN, INT_MAX = -2**31, 2**31 - 1
    
    # Get the sign of x and work with its absolute value
    sign = -1 if x < 0 else 1
    x = abs(x)
    
    # Reverse the digits
    reversed_x = int(str(x)[::-1])
    
    # Restore the sign
    reversed_x *= sign
    
    # Check for overflow
    if reversed_x < INT_MIN or reversed_x > INT_MAX:
        return 0
    
    return reversed_x

# Example Usage
print(reverse(123))     # Output: 321
print(reverse(-123))    # Output: -321
print(reverse(120))     # Output: 21
print(reverse(0))       # Output: 0